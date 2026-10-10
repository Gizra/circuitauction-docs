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

    def test_source_pages_skips_dot_directories(self):
        (self.tmp / ".superpowers").mkdir()
        (self.tmp / ".superpowers" / "x.md").write_text("# local only\n")
        self.assertEqual(common.source_pages(self.tmp), ["README.md", "client/README.md"])

    def test_language_dir_without_readme_is_still_a_language_dir(self):
        (self.tmp / "fr").mkdir()
        (self.tmp / "fr" / "_sidebar.md").write_text("* [Intro](/fr/README.md)\n")
        self.assertEqual(common.lang_dirs(self.tmp), ["de", "fr"])
        self.assertEqual(common.source_pages(self.tmp), ["README.md", "client/README.md"])

    def test_content_folder_named_like_a_language_is_not_a_language_dir(self):
        (self.tmp / "my-section").mkdir()
        (self.tmp / "my-section" / "x.md").write_text("# Section\n")
        self.assertEqual(common.lang_dirs(self.tmp), ["de"])
        self.assertIn("my-section/x.md", common.source_pages(self.tmp))

    def test_source_pages_excludes_it_section_and_maintainer_pages(self):
        (self.tmp / "it-section").mkdir()
        (self.tmp / "it-section" / "README.md").write_text("# IT\n")
        (self.tmp / "running-docs-locally.md").write_text("# Local\n")
        self.assertEqual(common.source_pages(self.tmp), ["README.md", "client/README.md"])

    def test_header_roundtrip(self):
        h = common.make_header("client/README.md", "0123456789ab")
        self.assertEqual(common.parse_header(h + "\n# x"), ("client/README.md", "0123456789ab"))
        self.assertIsNone(common.parse_header("# no header"))

    def test_sha_is_12_hex(self):
        self.assertRegex(common.sha_of(self.tmp / "README.md"), r"^[0-9a-f]{12}$")

    def test_rewrite_asset_links_is_depth_correct(self):
        text = "![](../assets/a.png) ![](assets/b.png) ![](../../assets/c.png) [x](/assets/d.png)"
        for page, prefix in (("tasks.md", "../"), ("auction/x.md", "../../"),
                             ("auction/clerk-screen/x.md", "../../../")):
            want = " ".join(f"![]({prefix}assets/{n}.png)" for n in "abc") + f" [x]({prefix}assets/d.png)"
            self.assertEqual(common.rewrite_asset_links(text, page), want, page)

    def test_rewrite_asset_links_handles_gitbook_and_angle_brackets(self):
        text = "![](../.gitbook/assets/a.png) ![](<../.gitbook/assets/b c.png>) ![](<../assets/d e.png>)"
        self.assertEqual(
            common.rewrite_asset_links(text, "items/x.md"),
            "![](../../.gitbook/assets/a.png) ![](<../../.gitbook/assets/b c.png>) ![](<../../assets/d e.png>)",
        )

    def test_rewrite_asset_links_handles_html_src(self):
        text = '<img src="../assets/x.png"> <video src=\'assets/y.mp4\'> <img src="/assets/z.png">'
        self.assertEqual(
            common.rewrite_asset_links(text, "client/x.md"),
            '<img src="../../assets/x.png"> <video src=\'../../assets/y.mp4\'> <img src="../../assets/z.png">',
        )

    def test_rewrite_asset_links_leaves_external_urls(self):
        text = "![](https://example.com/assets/a.png)"
        self.assertEqual(common.rewrite_asset_links(text, "tasks.md"), text)

    def test_has_misresolved_asset_links(self):
        f = common.has_misresolved_asset_links
        self.assertFalse(f("![](../../assets/a.png) ![](<../../.gitbook/assets/a b.png>)", "client/x.md"))
        self.assertFalse(f('<img src="../assets/a.png">', "tasks.md"))
        self.assertTrue(f("![](/assets/a.png)", "tasks.md"))
        self.assertTrue(f("![](../assets/a.png)", "client/x.md"))
        self.assertTrue(f("![](assets/a.png)", "tasks.md"))
        self.assertTrue(f("![](<../.gitbook/assets/a b.png>)", "client/x.md"))
        self.assertTrue(f('<img src="/assets/a.png">', "tasks.md"))

    def test_rewrite_sidebar_links(self):
        text = "* [Intro](README.md)\n* [Clients](client/README.md)\n* [Site](https://x.y/z.md)\n* [Abs](/de/x.md)"
        self.assertEqual(
            common.rewrite_sidebar_links(text, "de"),
            "* [Intro](/de/README.md)\n* [Clients](/de/client/README.md)\n* [Site](https://x.y/z.md)\n* [Abs](/de/x.md)",
        )

class PageLinkTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        make_repo(self.tmp)
        (self.tmp / "sale").mkdir()
        (self.tmp / "sale" / "x.md").write_text("# Sale\n")
        (self.tmp / "it").mkdir()
        (self.tmp / "it" / "y.md").write_text("# IT\n")
        (self.tmp / "de" / "client").mkdir()
        (self.tmp / "de" / "client" / "README.md").write_text("x\n")
        (self.tmp / "de" / "sale").mkdir()
        (self.tmp / "de" / "sale" / "x.md").write_text("x\n")

    def rw(self, text, page="client/README.md"):
        return common.rewrite_page_links(text, page, "de", self.tmp)

    def test_page_relative_and_root_relative_become_absolute_lang(self):
        self.assertEqual(self.rw("[a](../sale/x.md) [b](sale/x.md) [c](README.md)"),
                         "[a](/de/sale/x.md) [b](/de/sale/x.md) [c](/de/client/README.md)")

    def test_anchor_and_angle_brackets_kept(self):
        self.assertEqual(self.rw("[a](<../sale/x.md#s-1>)"), "[a](</de/sale/x.md#s-1>)")

    def test_untranslated_target_goes_to_english(self):
        self.assertEqual(self.rw("[a](../it/y.md#z)"), "[a](/it/y.md#z)")

    def test_external_absolute_image_and_unknown_unchanged(self):
        t = "[a](https://x.org/a.md) [b](mailto:a@b.md) [c](/sale/x.md) ![d](../sale/x.md) [e](nope.md)"
        self.assertEqual(self.rw(t), t)

    def test_has_relative_page_links(self):
        self.assertTrue(common.has_relative_page_links("[a](../x.md#h)"))
        self.assertTrue(common.has_relative_page_links("[a](<x.md>)"))
        self.assertFalse(common.has_relative_page_links("[a](/de/x.md) [b](https://a.b/c.md) ![i](x.md)"))


if __name__ == "__main__":
    unittest.main()
