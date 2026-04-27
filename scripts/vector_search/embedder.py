"""
嵌入生成抽象层 - 本地模型 + API 双模式
"""
from __future__ import annotations

import base64
import json
import struct
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Optional

from .config import VectorConfig


# ---------------------------------------------------------------------------
# 抽象接口
# ---------------------------------------------------------------------------

class Embedder(ABC):
    """所有嵌入器的公共接口。"""

    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        """将一批文本转为向量列表。返回 shape: (len(texts), dimension)。"""
        ...

    def is_available(self) -> bool:
        """检查当前嵌入器是否可以正常工作。"""
        try:
            self.embed(["test"])
            return True
        except Exception:
            return False


def get_embedder(config: VectorConfig) -> Embedder:
    """工厂函数：根据配置返回对应的嵌入器。"""
    if config.provider == "api":
        return APIEmbedder(config)
    return LocalEmbedder(config)


# ---------------------------------------------------------------------------
# 本地模型实现 (fastembed / onnxruntime)
# ---------------------------------------------------------------------------

class LocalEmbedder(Embedder):
    """
    本地模型嵌入器。
    优先使用 fastembed（自动下载/缓存模型）；
    如果指定了本地 model_path 且存在，从该路径加载。
    """

    def __init__(self, config: VectorConfig):
        self.config = config
        self._model: Any = None
        self._model_name = config.local_model_name
        self._model_path = config.local_model_path
        self._dimension = config.local_dimension
        self._max_length = config.local_max_length

    def _load(self):
        if self._model is not None:
            return
        try:
            from fastembed import TextEmbedding
        except ImportError as e:
            raise RuntimeError(
                "fastembed not installed. Run: pip install fastembed"
            ) from e

        # 若指定了本地路径且存在，fastembed 支持从本地加载
        kwargs: Dict[str, Any] = {
            "model_name": self._model_name,
            "max_length": self._max_length,
        }
        if self._model_path and Path(self._model_path).exists():
            kwargs["model_name"] = str(Path(self._model_path).resolve())

        self._model = TextEmbedding(**kwargs)

    def embed(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []
        self._load()
        # fastembed.embed 返回 numpy array 或迭代器，统一转成 Python list
        results = []
        for vec in self._model.embed(texts):
            if hasattr(vec, "tolist"):
                results.append(vec.tolist())
            else:
                results.append(list(vec))
        return results

    def is_available(self) -> bool:
        try:
            self._load()
            return True
        except Exception:
            return False


# ---------------------------------------------------------------------------
# API 实现 (OpenAI 兼容接口)
# ---------------------------------------------------------------------------

class APIEmbedder(Embedder):
    """
    远程 API 嵌入器。支持任何 OpenAI 兼容的嵌入接口。
    默认适配硅基流动 (siliconflow.cn)。
    """

    def __init__(self, config: VectorConfig):
        self.config = config
        self.base_url = config.api_base_url.rstrip("/")
        self.api_key = config.api_key
        self.model = config.api_model
        self.dimension = config.api_dimension
        self.batch_size = config.api_batch_size

        if not self.api_key:
            raise RuntimeError(
                "API key is empty. Set vector_search.api.api_key in config.json."
            )

    def embed(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []

        import urllib.request
        import ssl

        results: List[List[float]] = []
        # 分批处理
        for i in range(0, len(texts), self.batch_size):
            batch = texts[i : i + self.batch_size]
            payload = json.dumps({
                "model": self.model,
                "input": batch,
                "encoding_format": "float"
            }).encode("utf-8")

            req = urllib.request.Request(
                f"{self.base_url}/embeddings",
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}",
                },
                method="POST",
            )

            # 支持代理（如果环境变量中有 HTTP_PROXY）
            proxy = urllib.request.getproxies().get("https") or urllib.request.getproxies().get("http")
            if proxy:
                req.set_proxy(proxy.replace("http://", "").replace("https://", ""), "https")

            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            # OpenAI 格式: data[].embedding
            embeddings = sorted(data["data"], key=lambda x: x["index"])
            for item in embeddings:
                vec = item["embedding"]
                # 截断/填充到指定维度（防止模型实际输出与声明不一致）
                if len(vec) > self.dimension:
                    vec = vec[: self.dimension]
                elif len(vec) < self.dimension:
                    vec = vec + [0.0] * (self.dimension - len(vec))
                results.append(vec)

        return results

    def is_available(self) -> bool:
        try:
            self.embed(["ping"])
            return True
        except Exception:
            return False
