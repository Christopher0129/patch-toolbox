"""
配置读取与校验
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config.json"
SUPPORTED_PROVIDERS = {"local", "api"}
SUPPORTED_DISTANCE_METRICS = {"cosine", "l2"}


@dataclass
class VectorConfig:
    enabled: bool = False
    provider: str = "local"          # "local" | "api"

    # 本地模型参数
    local_model_name: str = "BAAI/bge-small-zh-v1.5"
    local_model_path: Optional[str] = None   # 若指定则优先从本地路径加载
    local_dimension: int = 512
    local_max_length: int = 512

    # API 参数
    api_base_url: str = "https://api.siliconflow.cn/v1"
    api_key: str = ""
    api_model: str = "BAAI/bge-m3"
    api_dimension: int = 1024
    api_batch_size: int = 32

    # 索引参数
    auto_index_on_run: bool = True
    index_batch_size: int = 64
    distance_metric: str = "cosine"   # cosine | l2

    # 搜索参数
    default_k: int = 10
    rrf_k: int = 60
    hybrid_weight_keywords: float = 0.4
    hybrid_weight_vector: float = 0.6

    @property
    def model_name(self) -> str:
        return self.local_model_name if self.provider == "local" else self.api_model

    @property
    def dimension(self) -> int:
        return self.local_dimension if self.provider == "local" else self.api_dimension

    @classmethod
    def load(cls, override: Optional[Dict[str, Any]] = None) -> "VectorConfig":
        """
        从顶层 config.json 读取配置，支持 override 字典（用于单元测试）。
        如果 config.json 不存在或没有 vector_search 字段，返回 enabled=False。
        """
        if override is None:
            if DEFAULT_CONFIG_PATH.exists():
                try:
                    with open(DEFAULT_CONFIG_PATH, "r", encoding="utf-8") as f:
                        root = json.load(f)
                    cfg = root.get("vector_search", {})
                except Exception:
                cfg = {}
            else:
                cfg = {}
        else:
            cfg = override

        # 递归替换 ${ENV_VAR} 占位符
        cfg = _deep_resolve_env(cfg)

        # 若 api_key 还是占位符（环境变量未设置），标记为无效
        api_key_value = cfg.get("api", {}).get("api_key", "")
        if api_key_value is None:
            api_key_resolved = ""
        elif isinstance(api_key_value, str):
            api_key_resolved = api_key_value
        else:
            raise ValueError("vector_search.api.api_key must be a string")
        if api_key_resolved.startswith("${") and api_key_resolved.endswith("}"):
            api_key_resolved = ""

        provider = cfg.get("provider", "local")
        if provider not in SUPPORTED_PROVIDERS:
            raise ValueError(f"Unsupported vector_search.provider: {provider}")

        distance_metric = cfg.get("index", {}).get("distance_metric", "cosine")
        if distance_metric not in SUPPORTED_DISTANCE_METRICS:
            raise ValueError(f"Unsupported vector_search.index.distance_metric: {distance_metric}")

        local_model_path = cfg.get("local", {}).get("model_path")
        if local_model_path:
            local_path = Path(local_model_path)
            if not local_path.is_absolute():
                local_model_path = str((PROJECT_ROOT / local_path).resolve())

        return cls(
            enabled=cfg.get("enabled", False),
            provider=provider,
            local_model_name=cfg.get("local", {}).get("model_name", "BAAI/bge-small-zh-v1.5"),
            local_model_path=local_model_path,
            local_dimension=cfg.get("local", {}).get("dimension", 512),
            local_max_length=cfg.get("local", {}).get("max_length", 512),
            api_base_url=cfg.get("api", {}).get("base_url", "https://api.siliconflow.cn/v1"),
            api_key=api_key_resolved,
            api_model=cfg.get("api", {}).get("model", "BAAI/bge-m3"),
            api_dimension=cfg.get("api", {}).get("dimension", 1024),
            api_batch_size=cfg.get("api", {}).get("batch_size", 32),
            auto_index_on_run=cfg.get("index", {}).get("auto_index_on_run", True),
            index_batch_size=cfg.get("index", {}).get("index_batch_size", 64),
            distance_metric=distance_metric,
            default_k=cfg.get("search", {}).get("default_k", 10),
            rrf_k=cfg.get("search", {}).get("rrf_k", 60),
            hybrid_weight_keywords=cfg.get("search", {}).get("hybrid_weight_keywords", 0.4),
            hybrid_weight_vector=cfg.get("search", {}).get("hybrid_weight_vector", 0.6),
        )


def _deep_resolve_env(obj):
    """递归替换字典/列表中的所有 ${ENV} 占位符。"""
    if isinstance(obj, dict):
        return {k: _deep_resolve_env(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_deep_resolve_env(v) for v in obj]
    return _resolve_env(obj)


def _resolve_env(value):
    """替换字符串中的 ${ENV_VAR} 为对应环境变量值。"""
    if not isinstance(value, str):
        return value
    import re
    pattern = re.compile(r"\$\{(\w+)\}")
    def replacer(m):
        env_key = m.group(1)
        return os.environ.get(env_key, m.group(0))
    return pattern.sub(replacer, value)
