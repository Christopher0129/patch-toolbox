"""Tests for sync_link_auditor.py — link topology expectations for the network-security platform split."""

from scripts.sync_link_auditor import EXPECTED_LINKS


class TestExpectedLinksNetworkSecurity:
    """Validate that EXPECTED_LINKS covers the network-security platform-split topology."""

    def test_network_security_index_has_expected_topology(self):
        assert "network-security/index.md" in EXPECTED_LINKS
        expected = EXPECTED_LINKS["network-security/index.md"]
        assert "windows.md" in expected, "index must link to windows.md"
        assert "linux.md" in expected, "index must link to linux.md"
        assert "macos.md" in expected, "index must link to macos.md"

    def test_network_security_child_pages_declared(self):
        for child in ("windows.md", "linux.md", "macos.md"):
            key = f"network-security/{child}"
            assert key in EXPECTED_LINKS, f"{key} must be in EXPECTED_LINKS"
            assert EXPECTED_LINKS[key] == ["index.md"], (
                f"{key} must link back to index.md, got {EXPECTED_LINKS[key]}"
            )

    def test_no_general_or_all_catchall_category(self):
        """Ensure no All/general catch-all category surfaces in the link topology."""
        for key in EXPECTED_LINKS:
            # network-security/index.md should only navigate to platform pages + README
            if key == "network-security/index.md":
                assert "windows.md" in EXPECTED_LINKS[key]
                assert "linux.md" in EXPECTED_LINKS[key]
                assert "macos.md" in EXPECTED_LINKS[key]
                # All/general must NOT appear
                for link in EXPECTED_LINKS[key]:
                    assert "all" not in link.lower()
                    assert "general" not in link.lower()
