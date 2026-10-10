import tempfile, unittest
from pathlib import Path

import common, scaffold
from tests.test_common import make_repo


class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        make_repo(self.tmp)

    def test_scaffold_page_writes_header_and_absolute_assets(self):
        dst = scaffold.scaffold_page(self.tmp, "de", "client/README.md")
        self.assertEqual(dst, self.tmp / "de" / "client" / "README.md")
        text = dst.read_text()
        self.assertEqual(common.parse_header(text),
                         ("client/README.md", common.sha_of(self.tmp / "client" / "README.md")))
        self.assertIn("![](/assets/screenshots/a.png)", text)

    def test_scaffold_page_never_overwrites(self):
        scaffold.scaffold_page(self.tmp, "de", "client/README.md")
        (self.tmp / "de" / "client" / "README.md").write_text("translated")
        self.assertIsNone(scaffold.scaffold_page(self.tmp, "de", "client/README.md"))
        self.assertEqual((self.tmp / "de" / "client" / "README.md").read_text(), "translated")

    def test_scaffold_sidebar_rewrites_links(self):
        dst = scaffold.scaffold_sidebar(self.tmp, "de")
        self.assertEqual(dst.read_text(), "* [Intro](/de/README.md)\n* [Clients](/de/client/README.md)\n")
        self.assertIsNone(scaffold.scaffold_sidebar(self.tmp, "de"))


if __name__ == "__main__":
    unittest.main()
