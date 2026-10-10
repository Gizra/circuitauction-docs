import tempfile, unittest
from pathlib import Path

import common


def make_repo(tmp: Path):
    (tmp / "client").mkdir()
    (tmp / "README.md").write_text("# Intro\n")
    (tmp / "_sidebar.md").write_text("* [Intro](README.md)\n* [Clients](client/README.md)\n")
    (tmp / "client" / "README.md").write_text("![](../assets/screenshots/a.png)\n")
    (tmp / "de").mkdir()
    (tmp / "de" / "README.md").write_text("# Einleitung\n")
    (tmp / "node_modules").mkdir()
    (tmp / "node_modules" / "x.md").write_text("junk\n")
    (tmp / "assets").mkdir()
    (tmp / "assets" / "note.md").write_text("junk\n")


class CommonTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        make_repo(self.tmp)

    def test_lang_dirs_finds_only_language_folders(self):
        self.assertEqual(common.lang_dirs(self.tmp), ["de"])

    def test_source_pages_skips_lang_dirs_non_content_and_vendor(self):
        self.assertEqual(common.source_pages(self.tmp), ["README.md", "client/README.md"])

    def test_header_roundtrip(self):
        h = common.make_header("client/README.md", "0123456789ab")
        self.assertEqual(common.parse_header(h + "\n# x"), ("client/README.md", "0123456789ab"))
        self.assertIsNone(common.parse_header("# no header"))

    def test_sha_is_12_hex(self):
        self.assertRegex(common.sha_of(self.tmp / "README.md"), r"^[0-9a-f]{12}$")

    def test_rewrite_asset_links(self):
        text = "![](../assets/a.png) ![](assets/b.png) ![](../../assets/c.png) [x](/assets/d.png)"
        self.assertEqual(
            common.rewrite_asset_links(text),
            "![](/assets/a.png) ![](/assets/b.png) ![](/assets/c.png) [x](/assets/d.png)",
        )

    def test_rewrite_sidebar_links(self):
        text = "* [Intro](README.md)\n* [Clients](client/README.md)\n* [Site](https://x.y/z.md)\n* [Abs](/de/x.md)"
        self.assertEqual(
            common.rewrite_sidebar_links(text, "de"),
            "* [Intro](/de/README.md)\n* [Clients](/de/client/README.md)\n* [Site](https://x.y/z.md)\n* [Abs](/de/x.md)",
        )


if __name__ == "__main__":
    unittest.main()
