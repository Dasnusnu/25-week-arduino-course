from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson13ContractTest(unittest.TestCase):
    def test_lesson_page_has_joystick_build_code_and_references(self):
        page = ROOT / "web" / "lessons" / "13-the-game-style-joystick.html"
        self.assertTrue(page.exists(), "Lesson 13 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Game-Style Joystick",
            "VRx → Arduino A0",
            "VRy → Arduino A1",
            "SW → Arduino D8",
            "INPUT_PULLUP",
            "analogRead(xAxisPin)",
            "analogRead(yAxisPin)",
            "digitalRead(switchPin)",
            "Serial.begin(9600)",
            "Reference pages",
            "13_Joystick.html",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-13" / "lesson-13-freenove-joystick-circuit.png"
        self.assertTrue(asset.is_file(), "Lesson 13 reference image is missing")
        page = (ROOT / "web" / "lessons" / "13-the-game-style-joystick.html").read_text(encoding="utf-8")
        self.assertIn("Freenove", page)
        self.assertIn("CC BY-NC-SA 3.0", page)
        self.assertIn("Chapter 13", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("13-the-game-style-joystick.html", index)


if __name__ == "__main__":
    unittest.main()
