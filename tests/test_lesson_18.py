from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson18ContractTest(unittest.TestCase):
    def test_lesson_page_has_source_validated_servo_wiring_code_safety_and_references(self):
        page = ROOT / "web" / "lessons" / "18-point-it-anywhere.html"
        self.assertTrue(page.exists(), "Lesson 18 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "Point It Anywhere",
            "Arduino A0 → potentiometer middle pin",
            "Arduino pin 3 → servo signal",
            "5 V → servo VCC",
            "GND → servo GND",
            "const byte servoPin = 3;",
            "const byte potPin = A0;",
            "map(rawReading, 0, 1023, 0, 180)",
            "pointerServo.write(angle);",
            "not safe to draw from an Arduino board",
            "Reference pages",
            "11_Servo.html",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-18" / "lesson-18-freenove-servo-pot-circuit.png"
        self.assertTrue(asset.is_file(), "Lesson 18 reference image is missing")
        page = (ROOT / "web" / "lessons" / "18-point-it-anywhere.html").read_text(encoding="utf-8")
        self.assertIn("Freenove", page)
        self.assertIn("CC BY-NC-SA 3.0", page)
        self.assertIn("Project 11.2", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("18-point-it-anywhere.html", index)


if __name__ == "__main__":
    unittest.main()
