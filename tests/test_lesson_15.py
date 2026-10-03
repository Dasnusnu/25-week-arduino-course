from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson15ContractTest(unittest.TestCase):
    def test_lesson_page_has_shift_register_build_code_and_references(self):
        page = ROOT / "web" / "lessons" / "15-more-lights-than-pins.html"
        self.assertTrue(page.exists(), "Lesson 15 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "More Lights Than Pins",
            "74HC595",
            "Arduino pin 11 → 74HC595 pin 14 (DS)",
            "Arduino pin 13 → 74HC595 pin 11 (SH_CP)",
            "Arduino pin 12 → 74HC595 pin 12 (ST_CP)",
            "pin 16 (VCC)",
            "pin 10 (MR)",
            "pin 8 (GND)",
            "pin 13 (OE)",
            "one 220 Ω resistor",
            "shiftOut(dataPin, clockPin, LSBFIRST, pattern)",
            "pattern &lt;&lt;= 1",
            "Reference pages",
            "15_LED_Matrix.html",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-15" / "lesson-15-freenove-74hc595-circuit.png"
        self.assertTrue(asset.is_file(), "Lesson 15 reference image is missing")
        page = (ROOT / "web" / "lessons" / "15-more-lights-than-pins.html").read_text(encoding="utf-8")
        self.assertIn("Freenove", page)
        self.assertIn("CC BY-NC-SA 3.0", page)
        self.assertIn("Project 15.1", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("15-more-lights-than-pins.html", index)


if __name__ == "__main__":
    unittest.main()
