import tempfile, unittest
from pathlib import Path

import glossary


class GlossaryTests(unittest.TestCase):
    def test_pairs_skip_identical_placeholders_and_long_strings(self):
        en = {"GENERAL": {"CLIENTS": "Clients", "SAVE": "Save", "HELLO": "Hello {{name}}",
                          "LONG": "x" * 61},
              "SALES": {"TITLE": "Sales", "CLIENTS": "Clients"}}
        de = {"GENERAL": {"CLIENTS": "Kunden", "SAVE": "Save", "HELLO": "Hallo {{name}}",
                          "LONG": "y" * 61},
              "SALES": {"TITLE": "Auktionen", "CLIENTS": "Klienten"}}
        self.assertEqual(glossary.glossary_pairs(en, de),
                         [("Clients", "Kunden"), ("Sales", "Auktionen")])

    def test_default_locale_dir_finds_sibling_checkout_from_worktree(self):
        tmp = Path(tempfile.mkdtemp())
        repo = tmp / "a" / "b" / "repo"
        repo.mkdir(parents=True)
        i18n = tmp / "a" / "circuitauction-backoffice" / "client" / "app" / "i18n"
        i18n.mkdir(parents=True)
        self.assertEqual(glossary.default_locale_dir(repo), i18n.resolve())

    def test_render_is_a_markdown_table(self):
        out = glossary.render([("Clients", "Kunden")], "de")
        self.assertIn("| English | de |", out)
        self.assertIn("| Clients | Kunden |", out)


if __name__ == "__main__":
    unittest.main()
