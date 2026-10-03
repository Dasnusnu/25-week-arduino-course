from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson07ContractTest(unittest.TestCase):
    def test_lesson_page_has_seven_segment_shift_register_build_and_references(self):
        page = ROOT / "web" / "lessons" / "07-make-numbers-appear.html"
        self.assertTrue(page.exists(), "Lesson 07 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "Make Numbers Appear",
            "1-digit 7-segment",
            "74HC595",
            "220 Ω",
            "latchPin = 12",
            "clockPin = 13",
            "dataPin = 11",
            "0xc0",
            "shiftOut(dataPin, clockPin, MSBFIRST, digits[i])",
            "Reference pages",
            "17_Digital_Display.html",
            "lesson-07-seven-segment-circuit.jpg",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_reference_asset_and_interactive_link_are_present(self):
        asset = ROOT / "web" / "assets" / "lesson-07" / "lesson-07-seven-segment-circuit.jpg"
        self.assertTrue(asset.is_file(), "Lesson 07 reference image is missing")
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("07-make-numbers-appear.html", index)


if __name__ == "__main__":
    unittest.main()
