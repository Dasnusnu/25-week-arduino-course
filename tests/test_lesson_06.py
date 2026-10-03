from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson06ContractTest(unittest.TestCase):
    def test_lesson_page_has_rgb_pwm_build_and_references(self):
        page = ROOT / "web" / "lessons" / "06-mix-your-own-colours.html"
        self.assertTrue(page.exists(), "Lesson 06 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "Mix Your Own Colours",
            "common-anode",
            "220 Ω",
            "pin 11",
            "pin 10",
            "pin 9",
            "analogWrite(redPin, 255 - red)",
            "analogWrite(greenPin, 255 - green)",
            "analogWrite(bluePin, 255 - blue)",
            "Reference pages",
            "8_RGB.html",
            "lesson-06-rgb-circuit.jpg",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_reference_asset_and_interactive_link_are_present(self):
        asset = ROOT / "web" / "assets" / "lesson-06" / "lesson-06-rgb-circuit.jpg"
        self.assertTrue(asset.is_file(), "Lesson 06 reference image is missing")
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("06-mix-your-own-colours.html", index)


if __name__ == "__main__":
    unittest.main()
