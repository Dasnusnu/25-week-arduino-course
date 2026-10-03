from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson02ContractTest(unittest.TestCase):
    def test_lesson_page_has_active_buzzer_build_and_references(self):
        page = ROOT / "web" / "lessons" / "02-make-some-noise.html"
        self.assertTrue(page.exists(), "Lesson 02 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "Make Some Noise",
            "active buzzer",
            "pin 12",
            "pin 9",
            "NPN transistor",
            "1 kΩ",
            "10 kΩ",
            "Reference pages",
            "9_Buzzer.html",
            "lesson-02-active-buzzer-circuit.jpg",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_reference_asset_and_interactive_link_are_present(self):
        asset = ROOT / "web" / "assets" / "lesson-02" / "lesson-02-active-buzzer-circuit.jpg"
        self.assertTrue(asset.is_file(), "Lesson 02 reference image is missing")
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("02-make-some-noise.html", index)


if __name__ == "__main__":
    unittest.main()
