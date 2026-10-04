from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson22ContractTest(unittest.TestCase):
    def test_lesson_page_has_authorized_rfid_wiring_read_only_code_safety_and_references(self):
        page = ROOT / "web" / "lessons" / "22-the-card-scanner.html"
        self.assertTrue(page.exists(), "Lesson 22 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Card Scanner",
            "RC522 3.3V → Arduino 3.3V",
            "RC522 GND → Arduino GND",
            "RC522 SDA (SS) → Arduino D10",
            "RC522 SCK → Arduino D13",
            "RC522 MOSI → Arduino D11",
            "RC522 MISO → Arduino D12",
            "RC522 RST → Arduino D9",
            "const byte ssPin = 10;",
            "const byte resetPin = 9;",
            "MFRC522 rfid(ssPin, resetPin);",
            "SPI.begin();",
            "rfid.PCD_Init();",
            "rfid.PICC_IsNewCardPresent()",
            "rfid.PICC_ReadCardSerial()",
            "rfid.PICC_HaltA();",
            "user-owned or lab RFID tags",
            "Do not use this lesson to clone",
            "Reference pages",
            "miguelbalboa/rfid",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-22" / "lesson-22-mit-rfid-wiring-table.png"
        self.assertTrue(asset.is_file(), "Lesson 22 reference image is missing")
        page = (ROOT / "web" / "lessons" / "22-the-card-scanner.html").read_text(encoding="utf-8")
        self.assertIn("RFID-Based Smart Door Lock System", page)
        self.assertIn("MIT License", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("22-the-card-scanner.html", index)


if __name__ == "__main__":
    unittest.main()
