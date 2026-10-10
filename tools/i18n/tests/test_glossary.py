import unittest

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

    def test_render_is_a_markdown_table(self):
        out = glossary.render([("Clients", "Kunden")], "de")
        self.assertIn("| English | de |", out)
        self.assertIn("| Clients | Kunden |", out)


if __name__ == "__main__":
    unittest.main()
