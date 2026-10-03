from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson16ContractTest(unittest.TestCase):
    def test_lesson_page_has_low_voltage_relay_build_code_and_references(self):
        page = ROOT / "web" / "lessons" / "16-small-board-big-switch.html"
        self.assertTrue(page.exists(), "Lesson 16 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "Small Board, Big Switch",
            "Arduino pin 12",
            "Arduino pin 9",
            "two AA batteries",
            "10 kΩ",
            "1 kΩ",
            "220 Ω",
            "flyback diode",
            "never connect this project to AC mains",
            "const byte relayPin = 9;",
            "const byte buttonPin = 12;",
            "if (buttonState == LOW)",
            "relayState = !relayState;",
            "Reference pages",
            "10_Motor.html",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-16" / "lesson-16-freenove-relay-circuit.png"
        self.assertTrue(asset.is_file(), "Lesson 16 reference image is missing")
        page = (ROOT / "web" / "lessons" / "16-small-board-big-switch.html").read_text(encoding="utf-8")
        self.assertIn("Freenove", page)
        self.assertIn("CC BY-NC-SA 3.0", page)
        self.assertIn("Project 10.1", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("16-small-board-big-switch.html", index)


if __name__ == "__main__":
    unittest.main()
