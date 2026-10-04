from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson25ContractTest(unittest.TestCase):
    def test_lesson_page_has_source_validated_wiring_safe_tag_notice_servo_pointer_and_references(self):
        page = ROOT / "web" / "lessons" / "25-the-rfid-door-lock.html"
        self.assertTrue(page.exists(), "Lesson 25 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The RFID Door Lock",
            "RC522 3.3V → Arduino 3.3V",
            "RC522 SDA (SS) → Arduino D10",
            "RC522 SCK → Arduino D13",
            "RC522 MOSI → Arduino D11",
            "RC522 MISO → Arduino D12",
            "RC522 RST → Arduino D9",
            "LCD VCC → Arduino 5V",
            "LCD GND → Arduino GND",
            "LCD SDA → Arduino A4 (SDA)",
            "LCD SCL → Arduino A5 (SCL)",
            "Arduino D3 → servo signal",
            "servo VCC → Arduino 5V",
            "servo GND → Arduino GND",
            "const byte servoPin = 3;",
            "rfid.PICC_IsNewCardPresent()",
            "rfid.PICC_ReadCardSerial()",
            "rfid.PICC_HaltA();",
            "pointerServo.write(tagSeenAngle);",
            "lcd.print(\"Tag seen\");",
            "bench/lab demonstrator",
            "Do not use this lesson to secure people or property",
            "Reference pages",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)
        for forbidden in (
            "authorizedUID",
            "Access Granted",
            "Access Denied",
            "Door is open",
            "unlock",
            "lockServo",
        ):
            self.assertNotIn(forbidden, content)

    def test_lesson_has_attributed_permitted_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-22" / "lesson-22-mit-rfid-wiring-table.png"
        self.assertTrue(asset.is_file(), "Retained MIT reference image is missing")
        page = (ROOT / "web" / "lessons" / "25-the-rfid-door-lock.html").read_text(encoding="utf-8")
        self.assertIn("RFID-Based Smart Door Lock System", page)
        self.assertIn("MIT License", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("25-the-rfid-door-lock.html", index)


if __name__ == "__main__":
    unittest.main()
