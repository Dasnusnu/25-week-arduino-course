from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson24ContractTest(unittest.TestCase):
    def test_lesson_page_has_combined_source_wiring_safe_scan_feedback_code_and_references(self):
        page = ROOT / "web" / "lessons" / "24-the-access-system.html"
        self.assertTrue(page.exists(), "Lesson 24 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Access System",
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
            "LiquidCrystal_I2C lcd(0x27, 16, 2);",
            "const byte ssPin = 10;",
            "const byte resetPin = 9;",
            "rfid.PICC_IsNewCardPresent()",
            "rfid.PICC_ReadCardSerial()",
            "rfid.PICC_HaltA();",
            "lcd.print(\"Tag seen\");",
            "lcd.print(\"Lab demo only\");",
            "user-owned or lab RFID tags",
            "Do not use this lesson to clone",
            "not an access-control system",
            "Reference pages",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)
        for forbidden in ("authorizedUID", "lockServo", "Servo.h", "Access Granted", "Access Denied", "Door is open"):
            self.assertNotIn(forbidden, content)

    def test_lesson_has_attributed_mit_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-22" / "lesson-22-mit-rfid-wiring-table.png"
        self.assertTrue(asset.is_file(), "Retained MIT reference image is missing")
        page = (ROOT / "web" / "lessons" / "24-the-access-system.html").read_text(encoding="utf-8")
        self.assertIn("RFID-Based Smart Door Lock System", page)
        self.assertIn("MIT License", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("24-the-access-system.html", index)


if __name__ == "__main__":
    unittest.main()
