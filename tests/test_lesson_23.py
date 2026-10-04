from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson23ContractTest(unittest.TestCase):
    def test_lesson_page_has_two_led_status_wiring_safe_demo_code_and_references(self):
        page = ROOT / "web" / "lessons" / "23-green-light-red-light.html"
        self.assertTrue(page.exists(), "Lesson 23 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "Green Light, Red Light",
            "Arduino D5 → green LED anode",
            "green LED cathode → 220 Ω resistor → Arduino GND",
            "Arduino D6 → red LED anode",
            "red LED cathode → 220 Ω resistor → Arduino GND",
            "const byte greenPin = 5;",
            "const byte redPin = 6;",
            "void showGreen()",
            "void showRed()",
            "digitalWrite(greenPin, HIGH);",
            "digitalWrite(redPin, HIGH);",
            "Serial.read()",
            "if (choice == 'g')",
            "else if (choice == 'r')",
            "lab/demo status indicator",
            "not an access-control system",
            "Do not use this lesson to unlock",
            "Reference pages",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_non_generated_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-23" / "lesson-23-freenove-led-circuit.jpg"
        self.assertTrue(asset.is_file(), "Lesson 23 reference image is missing")
        page = (ROOT / "web" / "lessons" / "23-green-light-red-light.html").read_text(encoding="utf-8")
        self.assertIn("Freenove", page)
        self.assertIn("CC BY-NC-SA 3.0", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("23-green-light-red-light.html", index)


if __name__ == "__main__":
    unittest.main()
