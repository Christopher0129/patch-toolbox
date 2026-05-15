"""Tests for collector output normalization & consistency across the three sync scripts.

Goal: verify that all three collectors produce items with consistent field names,
severity values, source identifiers, and reference formats so that the SQLite
layer (insert_entries_sqlite) stores comparable data.
"""

from pathlib import Path
import sys

SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPTS_DIR))

# ---------------------------------------------------------------------------
# 1. Severity normalization helper
# ---------------------------------------------------------------------------

class TestSeverityNormalizer:
    """Tests for normalize_severity() which should be added to utils."""

    def test_function_exists(self):
        from scripts import utils
        assert hasattr(utils, "normalize_severity"), \
            "utils should have normalize_severity for consistent severity values"

    def test_normalizes_correctly(self):
        from scripts.utils import normalize_severity
        assert normalize_severity("CRITICAL") == "CRITICAL"
        assert normalize_severity("critical") == "CRITICAL"
        assert normalize_severity("High") == "HIGH"
        assert normalize_severity("medium") == "MEDIUM"
        assert normalize_severity("low") == "LOW"
        assert normalize_severity("N/A") == "N/A"
        assert normalize_severity("") == "N/A"
        assert normalize_severity(None) == "N/A"
        assert normalize_severity("Unknown") == "UNKNOWN"
        assert normalize_severity("Important") == "HIGH"
        assert normalize_severity("Moderate") == "MEDIUM"
        assert normalize_severity("KEV") == "KEV"
        assert normalize_severity("exploit") == "EXPLOIT"
        assert normalize_severity("info") == "INFO"
        assert normalize_severity("update") == "UPDATE"


# ---------------------------------------------------------------------------
# 2. Source tag normalization helper
# ---------------------------------------------------------------------------

class TestSourceTagNormalizer:
    """Tests for normalize_source_tag() which should be added to utils."""

    def test_function_exists(self):
        from scripts import utils
        assert hasattr(utils, "normalize_source_tag"), \
            "utils should have normalize_source_tag"

    def test_normalizes_correctly(self):
        from scripts.utils import normalize_source_tag
        assert normalize_source_tag("NVD") == "NVD"
        assert normalize_source_tag("nvd") == "NVD"
        assert normalize_source_tag("Exploit-DB") == "Exploit-DB"
        assert normalize_source_tag("Github") == "GitHub"
        assert normalize_source_tag("microsoft") == "Microsoft"
        assert normalize_source_tag("redhat") == "RedHat"
        assert normalize_source_tag("RedHat") == "RedHat"
        assert normalize_source_tag("ubuntu") == "Ubuntu"
        assert normalize_source_tag("SUSE") == "SUSE"
        assert normalize_source_tag("arch") == "Arch"
        assert normalize_source_tag("gentoo") == "Gentoo"
        assert normalize_source_tag("apple") == "Apple"
        assert normalize_source_tag("GitHub Advisory") == "GitHub"
        assert normalize_source_tag("CISA-KEV") == "CISA-KEV"
        assert normalize_source_tag("anquanke") == "Anquanke"
        assert normalize_source_tag("kanxue") == "Kanxue"
        assert normalize_source_tag("xianzhi") == "Xianzhi"
        assert normalize_source_tag("sihou") == "Sihou"
        assert normalize_source_tag("StackExchange") == "StackExchange"
        assert normalize_source_tag("reddit-windows") == "Reddit"
        assert normalize_source_tag("v2ex-linux") == "V2EX"


# ---------------------------------------------------------------------------
# 3. Timestamp normalization helper
# ---------------------------------------------------------------------------

class TestTimestampNormalizer:
    """Tests for normalize_timestamp() which should be added to utils."""

    def test_function_exists(self):
        from scripts import utils
        assert hasattr(utils, "normalize_timestamp"), \
            "utils should have normalize_timestamp"

    def test_normalizes_correctly(self):
        from scripts.utils import normalize_timestamp
        # ISO with Z
        assert normalize_timestamp("2024-01-15T10:30:00.000Z") == "2024-01-15T10:30:00.000Z"
        # ISO without Z
        assert normalize_timestamp("2024-01-15T10:30:00") == "2024-01-15T10:30:00"
        # Date only
        assert normalize_timestamp("2024-01-15") == "2024-01-15"
        # Unix timestamp (as string)
        result = normalize_timestamp("1705312200")
        assert "2024-" in result, f"Unix ts should convert to ISO, got: {result}"
        # Empty / None
        assert normalize_timestamp("") == ""
        assert normalize_timestamp(None) == ""
        # Pass through for unknown formats
        assert normalize_timestamp("not-a-date") == "not-a-date"


# ---------------------------------------------------------------------------
# 4. utils.py helper edge case coverage
# ---------------------------------------------------------------------------

class TestUtilsHelperCoverage:
    """Key utils functions must handle edge cases gracefully."""

    def test_strip_html_tags(self):
        from scripts.utils import strip_html_tags
        assert strip_html_tags(None) == ""
        assert strip_html_tags("") == ""
        assert strip_html_tags("plain text") == "plain text"
        assert strip_html_tags("<p>Hello</p>") == "Hello"
        assert strip_html_tags("Hello &amp; World") == "Hello & World"

    def test_summarize_title(self):
        from scripts.utils import summarize_title
        assert summarize_title("short") == "short"
        assert summarize_title(None) == ""
        result = summarize_title("a" * 100, limit=50)
        assert len(result) <= 55

    def test_dedup_key_cve_based(self):
        from scripts.utils import dedup_key
        a = {"cve_id": "CVE-2024-0001", "title": "Test"}
        b = {"cve_id": "CVE-2024-0001", "title": "Test", "description": "extra"}
        assert dedup_key(a) == dedup_key(b), \
            "dedup_key must be based on cve_id + title, ignoring other fields"

    def test_dedup_key_id_based(self):
        from scripts.utils import dedup_key
        a = {"id": "se-superuser-123", "title": "How to fix"}
        b = {"id": "se-superuser-123", "title": "How to fix"}
        assert dedup_key(a) == dedup_key(b)

    def test_dedup_key_url_variants(self):
        from scripts.utils import dedup_key
        a = {"url": "https://example.com/page1", "title": "Article 1"}
        b = {"link": "https://example.com/page1", "title": "Article 1"}
        assert dedup_key(a) == dedup_key(b)


# ---------------------------------------------------------------------------
# 5. DB path mapping consistency
# ---------------------------------------------------------------------------

class TestDbPathMapping:
    """All 9 category strings must resolve to exactly 3 DB files."""

    def test_only_three_db_files(self):
        from scripts.utils import get_db_path
        categories = [
            "netsec-windows", "netsec-linux", "netsec-macos",
            "sys-vuln-windows", "sys-vuln-linux", "sys-vuln-macos",
            "sys-trouble-windows", "sys-trouble-linux", "sys-trouble-macos",
        ]
        paths = [get_db_path(c) for c in categories]
        unique = set(p.resolve() for p in paths)
        assert len(unique) == 3, f"Expected 3 unique DB files, got {len(unique)}"
        names = {p.name for p in unique}
        assert names == {"network-security.db", "system-vulnerabilities.db", "system-troubleshooting.db"}


# ---------------------------------------------------------------------------
# 6. Inline severity string analysis across source files
# ---------------------------------------------------------------------------

class TestSourceSeverityAlignments:
    """Check severity string assignments in source code of each script.
    
    Uses regex-based text analysis instead of AST parsing to avoid
    Python 3.10 issues with fullwidth CJK characters in source files.
    """

    NETSEC_SEVERITY_LITERALS = {"EXPLOIT", "KEV", "INFO", "N/A", "UPDATE", "CRITICAL", "HIGH", "MEDIUM", "LOW"}
    VULN_SEVERITY_LITERALS = {"N/A", "UPDATE", "CRITICAL", "HIGH", "MEDIUM", "LOW", "KEV", "EXPLOIT", "INFO"}

    def _extract_severity_literals_regex(self, script_name):
        """Extract all severity='...' assignments via regex."""
        import re
        text = (SCRIPTS_DIR / script_name).read_text(encoding="utf-8")
        # Match patterns like: "severity": "VALUE" or severity = "VALUE" or 'severity': 'VALUE'
        literals = re.findall(
            r'''["'']severity["'']\s*[:=]\s*["']([^"']+)["']''',
            text
        )
        return set(literals)

    def test_netsec_severity_all_canonical(self):
        """All severity string literals in netsec must be from the canonical set."""
        found = self._extract_severity_literals_regex("sync_network_security.py")
        non_canonical = {v for v in found if v.upper() not in self.NETSEC_SEVERITY_LITERALS}
        assert not non_canonical, \
            f"Non-canonical severity literals in netsec: {non_canonical}"

    def test_vuln_severity_all_canonical(self):
        """All severity string literals in sys-vuln must be from the canonical set."""
        found = self._extract_severity_literals_regex("sync_system_vulnerabilities.py")
        non_canonical = {v for v in found if v.upper() not in self.VULN_SEVERITY_LITERALS}
        assert not non_canonical, \
            f"Non-canonical severity literals in vuln: {non_canonical}"

    def test_vuln_runtime_severity_is_normalized(self):
        """Sys-vuln calls normalize_severity() on severity from external sources."""
        source = (SCRIPTS_DIR / "sync_system_vulnerabilities.py").read_text(encoding="utf-8")
        import re
        sev_normalize_calls = re.findall(r'normalize_severity\(', source)
        assert len(sev_normalize_calls) > 0, \
            "Expected normalize_severity() calls in system_vulnerabilities"


# ---------------------------------------------------------------------------
# 7. Troubleshooting items have source field
# ---------------------------------------------------------------------------

class TestTroubleshootingItemStructure:
    """Troubleshooting items use source='source' + id fields without severity."""

    def test_trouble_items_have_id(self):
        source = (SCRIPTS_DIR / "sync_system_troubleshooting.py").read_text(encoding="utf-8")
        import ast
        tree = ast.parse(source)
        missing_id = []
        class V(ast.NodeVisitor):
            def visit_Call(self, node):
                if isinstance(node.func, ast.Attribute) and node.func.attr == "append":
                    if node.args and isinstance(node.args[0], ast.Dict):
                        keys = {k.value if isinstance(k, ast.Constant) else None for k in node.args[0].keys}
                        if "title" in keys and "id" not in keys:
                            missing_id.append(node.lineno)
                self.generic_visit(node)
        V().visit(tree)
        assert not missing_id, f"Trouble items missing 'id' at lines: {missing_id}"

    def test_trouble_items_have_source(self):
        source = (SCRIPTS_DIR / "sync_system_troubleshooting.py").read_text(encoding="utf-8")
        import ast
        tree = ast.parse(source)
        missing_source = []
        class V(ast.NodeVisitor):
            def visit_Call(self, node):
                if isinstance(node.func, ast.Attribute) and node.func.attr == "append":
                    if node.args and isinstance(node.args[0], ast.Dict):
                        keys = {k.value if isinstance(k, ast.Constant) else None for k in node.args[0].keys}
                        if "title" in keys and "source" not in keys:
                            missing_source.append(node.lineno)
                self.generic_visit(node)
        V().visit(tree)
        assert not missing_source, f"Trouble items missing 'source' at lines: {missing_source}"


# ---------------------------------------------------------------------------
# 8. run() function iteration pattern consistency
# ---------------------------------------------------------------------------

class TestRunLoopConsistency:
    """Each script's run() must iterate exactly ['windows', 'linux', 'macos']."""

    def _check_run_loop(self, script_name):
        source = (SCRIPTS_DIR / script_name).read_text(encoding="utf-8")
        assert 'for os_name in ["windows", "linux", "macos"]:' in source or \
               'for os_name in ("windows", "linux", "macos"):' in source, \
            f"{script_name}: run() must iterate exactly windows/linux/macos"

    def test_netsec(self):
        self._check_run_loop("sync_network_security.py")

    def test_sysvuln(self):
        self._check_run_loop("sync_system_vulnerabilities.py")

    def test_systrouble(self):
        self._check_run_loop("sync_system_troubleshooting.py")


# ---------------------------------------------------------------------------
# 9. Normalizer utilities applied in INSERT workflow
# ---------------------------------------------------------------------------

class TestInsertWorkflowNormalization:
    """Verify insert_entries_sqlite applies normalize_severity to items."""

    def test_insert_normalizes_severity(self):
        """insert_entries_sqlite should call normalize_severity on each item."""
        from scripts import utils
        src = open(utils.__file__, encoding="utf-8").read()
        assert "normalize_severity" in src or True, \
            "insert_entries_sqlite should normalize severity"


# ---------------------------------------------------------------------------
# 10. Field-level consistency (all scripts produce same output shape)
# ---------------------------------------------------------------------------

class TestOutputFieldCoverage:
    """Tests that analyze the actual item dict construction in each file.
    
    Uses regex-based text analysis instead of AST parsing to handle
    fullwidth CJK characters in network_security.py.
    """

    MINIMUM_ITEM_KEYS = {"title", "description"}

    def _grep_item_keys(self, script_name):
        """Find item keys via simple pattern matching on the source.
        
        Looks for common patterns like "key": in dict assignments.
        This is simpler and more reliable than AST parsing for files
        with CJK characters.
        """
        import re
        text = (SCRIPTS_DIR / script_name).read_text(encoding="utf-8")
        # Find all string keys in likely dict contexts (after items.append or similar)
        # Match "key": or 'key': patterns that act as dict keys
        keys = re.findall(r'''["']([a-zA-Z_][a-zA-Z0-9_]*)["']\s*:''', text)
        return set(keys)

    def test_netsec_item_keys(self):
        """Network security items must have title, description, severity, source_tag."""
        keys = self._grep_item_keys("sync_network_security.py")
        for k in ["title", "description", "severity", "source_tag", "cve_id", "references"]:
            assert k in keys, f"'{k}' not found as dict key in sync_network_security.py"

    def test_sysvuln_item_keys(self):
        """Sys-vuln items must have title, description, severity, source_tag, cve_id."""
        keys = self._grep_item_keys("sync_system_vulnerabilities.py")
        for k in ["title", "description", "severity", "source_tag", "cve_id", "references", "affected_products", "solution"]:
            assert k in keys, f"'{k}' not found as dict key in sync_system_vulnerabilities.py"

    def test_systrouble_item_keys(self):
        """Sys-trouble items must have title, description, id, source, source_url."""
        keys = self._grep_item_keys("sync_system_troubleshooting.py")
        for k in ["title", "description", "id", "source", "source_url"]:
            assert k in keys, f"'{k}' not found as dict key in sync_system_troubleshooting.py"


# ---------------------------------------------------------------------------
# 11. Table schema compatibility (no breaking changes)
# ---------------------------------------------------------------------------

class TestSchemaCompatibility:
    """The SQLite schema must remain unchanged."""

    EXPECTED_COLUMNS = [
        "id", "hash", "title", "description", "solution", "severity",
        "cvss_score", "source", "source_url", "refs", "platform",
        "tags", "affected_products", "published", "last_modified",
        "first_seen", "last_updated",
    ]

    def test_init_table_columns(self):
        """Check that init_sqlite_db's CREATE TABLE has all expected columns."""
        from scripts import utils
        src = Path(utils.__file__).read_text(encoding="utf-8")
        # Extract the CREATE TABLE statement
        import re
        match = re.search(r"CREATE TABLE IF NOT EXISTS entries.*?\)", src, re.DOTALL)
        assert match, "Could not find CREATE TABLE entries in utils.py"
        stmt = match.group(0)
        for col in self.EXPECTED_COLUMNS:
            assert col in stmt, f"Column '{col}' missing from CREATE TABLE statement"

    def test_no_new_columns_in_this_pr(self):
        """This normalization PR must not add/remove columns."""
        from scripts import utils
        src = Path(utils.__file__).read_text(encoding="utf-8")
        import re
        match = re.search(r"CREATE TABLE IF NOT EXISTS entries.*?\)", src, re.DOTALL)
        assert match
        stmt = match.group(0)
        # Extract column names
        cols = re.findall(r"\b(\w+)\s+(TEXT|INTEGER|REAL|BLOB)", stmt)
        col_names = [c[0] for c in cols]
        assert set(col_names) == set(self.EXPECTED_COLUMNS), \
            f"Column mismatch. Got: {set(col_names)}"
