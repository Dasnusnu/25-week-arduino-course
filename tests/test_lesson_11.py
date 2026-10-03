from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson11ContractTest(unittest.TestCase):
    def test_lesson_page_has_i2c_lcd_build_code_and_references(self):
        page = ROOT / "web" / "lessons" / "11-words-on-a-real-screen.html"
        self.assertTrue(page.exists(), "Lesson 11 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "Words on a Real Screen",
            "I2C LCD1602",
            "Arduino 5V",
            "Arduino GND",
            "Arduino A4 (SDA)",
            "Arduino A5 (SCL)",
            "LiquidCrystal_I2C lcd(0x27, 16, 2)",
            "LiquidCrystal_I2C(0x3F, 16, 2)",
            "lcd.init()",
            "lcd.backlight()",
            "lcd.setCursor(0, 1)",
            "lcd.print(\"HELLO, MAKER!\")",
            "millis() / 1000",
            "Reference pages",
            "16_LCD1602.html",
            "lesson-11-freenove-i2c-lcd1602-circuit.png",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-11" / "lesson-11-freenove-i2c-lcd1602-circuit.png"
        self.assertTrue(asset.is_file(), "Lesson 11 reference image is missing")
        page = (ROOT / "web" / "lessons" / "11-words-on-a-real-screen.html").read_text(encoding="utf-8")
        self.assertIn("Freenove", page)
        self.assertIn("CC BY-NC-SA 3.0", page)
        self.assertIn("Chapter 16", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("11-words-on-a-real-screen.html", index)


if __name__ == "__main__":
    unittest.main()
