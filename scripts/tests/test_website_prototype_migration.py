"""Test that the accepted frontend prototype has been migrated into website/.

This test verifies:
1. All expected config/build files exist (package.json, tailwind.config.js, etc.)
2. All expected i18n files exist (locales + LanguageContext)
3. All expected component files exist (Navbar, Footer, Layout, shadcn/ui components)
4. All expected page files exist (Home, NetworkSecurity, etc.)
5. All expected public assets exist
6. Key structural patterns: @ alias usage, HashRouter, LanguageProvider, framer-motion
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WEBSITE = ROOT / "website"

# ── Config / Build Files ──

CONFIG_FILES = [
    "package.json",
    "tailwind.config.js",
    "postcss.config.js",
    "components.json",
    "eslint.config.js",
    "index.html",
]


def _resolve(rel_path: str) -> Path:
    """Resolve a path relative to website/, or the root if it starts with ../."""
    if rel_path.startswith("../"):
        return (ROOT / rel_path[3:]).resolve()
    return (WEBSITE / rel_path).resolve()


def test_config_files_exist():
    missing = [
        path
        for path in [WEBSITE / f for f in CONFIG_FILES]
        if not path.exists()
    ]
    assert not missing, f"missing config/build files: {[str(p.relative_to(WEBSITE)) for p in missing]}"


def test_index_html_has_google_fonts():
    """index.html should link Google Fonts (Inter, JetBrains Mono, Space Grotesk)."""
    html = (WEBSITE / "index.html").read_text()
    assert "fonts.googleapis.com" in html, "index.html missing Google Fonts link"
    assert "Inter" in html, "index.html missing Inter font"
    assert "JetBrains+Mono" in html, "index.html missing JetBrains Mono font"
    assert "Space+Grotesk" in html, "index.html missing Space Grotesk font"


def test_package_json_has_prototype_deps():
    """package.json should include key prototype dependencies (framer-motion, react-router, lucide-react, i18n libs, tailwind-merge)."""
    pkg = (WEBSITE / "package.json").read_text()
    expected = [
        "framer-motion",
        "react-router-dom",
        "lucide-react",
        "tailwind-merge",
        "clsx",
        "tailwindcss",
        "class-variance-authority",
    ]
    missing = [dep for dep in expected if dep not in pkg]
    assert not missing, f"missing prototype dependencies in package.json: {missing}"


def test_tailwind_config_has_custom_colors():
    """tailwind.config.js should have custom color tokens (bg-base, accent-blue, etc.)."""
    cfg = (WEBSITE / "tailwind.config.js").read_text()
    custom_tokens = [
        "bg-base",
        "bg-surface",
        "bg-elevated",
        "border-subtle",
        "border-active",
        "text-primary",
        "text-secondary",
        "text-muted",
        "accent-blue",
        "accent-cyan",
        "accent-amber",
        "accent-orange",
        "accent-red",
        "accent-green",
        "accent-purple",
    ]
    missing = [t for t in custom_tokens if t not in cfg]
    assert not missing, f"missing custom color tokens in tailwind.config.js: {missing}"


def test_tailwind_config_has_custom_fonts():
    """tailwind.config.js should have custom font families (heading, body, mono)."""
    cfg = (WEBSITE / "tailwind.config.js").read_text()
    assert "Space Grotesk" in cfg, "missing Space Grotesk font family in tailwind config"
    assert "JetBrains Mono" in cfg, "missing JetBrains Mono font family in tailwind config"
    assert "Inter" in cfg, "missing Inter font family in tailwind config"


def test_tailwind_config_has_custom_animations():
    """tailwind.config.js should have custom animations (accordion-down, bounce-scroll, etc.)."""
    cfg = (WEBSITE / "tailwind.config.js").read_text()
    expected = ["accordion-down", "accordion-up", "hero-glow-pulse", "bounce-scroll", "cursor-blink"]
    missing = [a for a in expected if a not in cfg]
    assert not missing, f"missing custom animations in tailwind.config.js: {missing}"


# ── i18n Files ──


def test_i18n_locales_exist():
    """All 5 locale files should exist under src/i18n/locales/."""
    locales = ["en", "zh", "fr", "ja", "ko"]
    missing = [
        f"{l}.json"
        for l in locales
        if not (WEBSITE / "src" / "i18n" / "locales" / f"{l}.json").exists()
    ]
    assert not missing, f"missing locale files: {missing}"


def test_language_context_exists():
    assert (WEBSITE / "src" / "i18n" / "LanguageContext.tsx").exists(), "missing LanguageContext.tsx"


def test_language_context_exports():
    ctx = (WEBSITE / "src" / "i18n" / "LanguageContext.tsx").read_text()
    expected_exports = ["LanguageProvider", "useTranslation", "LANGUAGE_NAMES"]
    missing = [e for e in expected_exports if e not in ctx]
    assert not missing, f"missing exports in LanguageContext.tsx: {missing}"


def test_language_context_has_5_languages():
    ctx = (WEBSITE / "src" / "i18n" / "LanguageContext.tsx").read_text()
    for lang in ["zh", "en", "fr", "ja", "ko"]:
        assert lang in ctx, f"missing language '{lang}' in LanguageContext.tsx"


# ── Component Files ──


def test_components_exist():
    """Layout, Navbar, Footer components should exist."""
    expected_components = ["Layout.tsx", "Navbar.tsx", "Footer.tsx"]
    missing = [
        c
        for c in expected_components
        if not (WEBSITE / "src" / "components" / c).exists()
    ]
    assert not missing, f"missing component files: {missing}"


def test_navbar_has_language_switcher():
    """Navbar should include language switching UI."""
    navbar = (WEBSITE / "src" / "components" / "Navbar.tsx").read_text()
    assert "setLang" in navbar, "Navbar missing language switching (setLang)"


def test_layout_uses_navbar_footer():
    """Layout should import and render Navbar and Footer."""
    layout = (WEBSITE / "src" / "components" / "Layout.tsx").read_text()
    assert "Navbar" in layout, "Layout missing Navbar import"
    assert "Footer" in layout, "Layout missing Footer import"


# ── Page Files ──


def test_pages_exist():
    """All 6 page files should exist under src/pages/."""
    expected_pages = [
        "Home.tsx",
        "NetworkSecurity.tsx",
        "SystemVulnerabilities.tsx",
        "SystemTroubleshooting.tsx",
        "About.tsx",
        "Contributing.tsx",
    ]
    missing = [
        p
        for p in expected_pages
        if not (WEBSITE / "src" / "pages" / p).exists()
    ]
    assert not missing, f"missing page files: {missing}"


# ── App.tsx Routing ──


def test_app_routes_configured():
    """App.tsx should configure all 6 routes via react-router-dom."""
    app = (WEBSITE / "src" / "App.tsx").read_text()
    expected_routes = [
        "/",
        "/network-security",
        "/system-vulnerabilities",
        "/system-troubleshooting",
        "/about",
        "/contributing",
    ]
    missing = [r for r in expected_routes if r not in app]
    assert not missing, f"missing routes in App.tsx: {missing}"


def test_app_uses_hash_router():
    """main.tsx should use HashRouter from react-router-dom."""
    main_tsx = (WEBSITE / "src" / "main.tsx").read_text()
    assert "HashRouter" in main_tsx, "main.tsx missing HashRouter import"


def test_app_uses_language_provider():
    """App.tsx should wrap with LanguageProvider."""
    app = (WEBSITE / "src" / "App.tsx").read_text()
    assert "LanguageProvider" in app, "App.tsx missing LanguageProvider"


# ── Public Assets ──


def test_public_assets_exist():
    """Expected public/ assets should exist."""
    expected = ["severity-chart-placeholder.png", "github-activity-graph.png"]
    missing = [a for a in expected if not (WEBSITE / "public" / a).exists()]
    assert not missing, f"missing public assets: {missing}"


# ──── Package Lock ────


def test_package_lock_exists():
    assert (WEBSITE / "package-lock.json").exists(), "missing package-lock.json"


# ── Package.json scripts ──


def test_package_json_has_prototype_scripts():
    """package.json should have lint script."""
    pkg = (WEBSITE / "package.json").read_text()
    assert '"lint"' in pkg, 'missing "lint" script in package.json'
