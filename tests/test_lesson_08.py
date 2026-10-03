from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson08ContractTest(unittest.TestCase):
    def test_lesson_page_has_four_digit_counter_build_and_references(self):
        page = ROOT / "web" / "lessons" / "08-the-counting-machine.html"
        self.assertTrue(page.exists(), "Lesson 08 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Counting Machine",
            "4-digit 7-segment",
            "74HC595",
            "220 Ω",
            "const int commonPins[] = {7, 6, 5, 4}",
            "const int latchPin = 12",
            "const int clockPin = 13",
            "const int dataPin = 11",
            "shiftOut(dataPin, clockPin, LSBFIRST, value)",
            "writeData(digits[digit])",
            "writeData(0xff)",
            "elapsedSeconds % 10000UL",
            "Reference pages",
            "17_Digital_Display.html",
            "lesson-08-four-digit-seven-segment-circuit.jpg",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_reference_asset_and_interactive_link_are_present(self):
        asset = ROOT / "web" / "assets" / "lesson-08" / "lesson-08-four-digit-seven-segment-circuit.jpg"
        self.assertTrue(asset.is_file(), "Lesson 08 reference image is missing")
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("08-the-counting-machine.html", index)


if __name__ == "__main__":
    unittest.main()
