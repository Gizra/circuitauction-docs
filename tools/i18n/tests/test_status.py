import tempfile, unittest
from pathlib import Path

import scaffold, status
from tests.test_common import make_repo


class StatusTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        make_repo(self.tmp)
        (self.tmp / "sale").mkdir()
        (self.tmp / "sale" / "x.md").write_text("# Sale\n")

    def test_categories(self):
        scaffold.scaffold_page(self.tmp, "de", "client/README.md")           # untranslated copy
        p = scaffold.scaffold_page(self.tmp, "de", "sale/x.md")
        p.write_text(p.read_text().replace("# Sale", "# Verkauf"))           # translated, current
        (self.tmp / "sale" / "x.md").write_text("# Sale (edited)\n")         # ... now outdated
        (self.tmp / "de" / "orphan.md").write_text("<!-- i18n source=gone.md sha=000000000000 -->\n")
        (self.tmp / "de" / "README.md").write_text("<!-- i18n source=README.md sha=000000000000 -->\n![](../assets/a.png)\n")
        r = status.status(self.tmp, "de")
        self.assertEqual(r["untranslated"], ["client/README.md"])
        self.assertEqual(r["outdated"], ["README.md", "sale/x.md"])
        self.assertEqual(r["missing"], [])
        self.assertEqual(r["orphan"], ["de/orphan.md"])
        self.assertEqual(r["broken-assets"], ["README.md"])
        self.assertEqual(r["current"], [])

    def test_scaffolded_only_language_folder_is_not_treated_as_source(self):
        (self.tmp / "de" / "README.md").unlink()
        scaffold.scaffold_page(self.tmp, "de", "client/README.md")
        r = status.status(self.tmp, "de")
        self.assertEqual(r["untranslated"], ["client/README.md"])
        self.assertEqual(r["missing"], ["README.md", "sale/x.md"])
        self.assertEqual(r["orphan"], [])
        self.assertFalse([e for cat in r.values() for e in cat if e.startswith("de/")])

    def test_missing_and_no_header_is_outdated(self):
        (self.tmp / "de" / "README.md").write_text("# Einleitung\n")
        r = status.status(self.tmp, "de")
        self.assertEqual(r["missing"], ["client/README.md", "sale/x.md"])
        self.assertEqual(r["outdated"], ["README.md"])


if __name__ == "__main__":
    unittest.main()
