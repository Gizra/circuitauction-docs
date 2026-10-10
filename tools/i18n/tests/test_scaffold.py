import tempfile, unittest
from pathlib import Path

import common, scaffold
from tests.test_common import make_repo


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        make_repo(self.tmp)

    def test_scaffold_page_writes_header_and_depth_correct_assets(self):
        dst = scaffold.scaffold_page(self.tmp, "de", "client/README.md")
        self.assertEqual(dst, self.tmp / "de" / "client" / "README.md")
        text = dst.read_text()
        self.assertEqual(common.parse_header(text),
                         ("client/README.md", common.sha_of(self.tmp / "client" / "README.md")))
        self.assertIn("![](../../assets/screenshots/a.png)", text)

    def test_scaffold_page_rewrites_page_links_to_absolute(self):
        (self.tmp / "client" / "README.md").write_text("[i](../README.md#a) ![](../assets/screenshots/a.png)\n")
        text = scaffold.scaffold_page(self.tmp, "de", "client/README.md").read_text()
        self.assertIn("[i](/de/README.md#a)", text)

    def test_scaffold_page_never_overwrites(self):
        scaffold.scaffold_page(self.tmp, "de", "client/README.md")
        (self.tmp / "de" / "client" / "README.md").write_text("translated")
        self.assertIsNone(scaffold.scaffold_page(self.tmp, "de", "client/README.md"))
        self.assertEqual((self.tmp / "de" / "client" / "README.md").read_text(), "translated")

    def test_scaffold_sidebar_rewrites_links(self):
        dst = scaffold.scaffold_sidebar(self.tmp, "de")
        self.assertEqual(dst.read_text(), "* [Intro](/de/README.md)\n* [Clients](/de/client/README.md)\n")
        self.assertIsNone(scaffold.scaffold_sidebar(self.tmp, "de"))

    def test_validate_rejects_bad_lang_and_pages(self):
        with self.assertRaises(ValueError):
            scaffold.validate(self.tmp, "DE", ["README.md"])
        for bad in ("de/README.md", "docs/x.md", "MAINTAINING_DOCS.md", "nope.md"):
            with self.assertRaises(ValueError, msg=bad):
                scaffold.validate(self.tmp, "de", [bad])
        scaffold.validate(self.tmp, "de", ["README.md", "client/README.md"])

    def test_restamp_rewrites_only_header(self):
        scaffold.scaffold_page(self.tmp, "de", "client/README.md")
        dst = self.tmp / "de" / "client" / "README.md"
        dst.write_text("<!-- i18n source=client/README.md sha=000000000000 -->\nÜbersetzt\n")
        scaffold.restamp_page(self.tmp, "de", "client/README.md")
        self.assertEqual(dst.read_text(),
                         common.make_header("client/README.md", common.sha_of(self.tmp / "client" / "README.md"))
                         + "\nÜbersetzt\n")

    def test_restamp_refuses_missing_or_headerless(self):
        with self.assertRaises(ValueError):
            scaffold.restamp_page(self.tmp, "de", "client/README.md")
        (self.tmp / "de" / "client").mkdir()
        (self.tmp / "de" / "client" / "README.md").write_text("no header\n")
        with self.assertRaises(ValueError):
            scaffold.restamp_page(self.tmp, "de", "client/README.md")


if __name__ == "__main__":
    unittest.main()
