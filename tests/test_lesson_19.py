from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson19ContractTest(unittest.TestCase):
    def test_lesson_page_has_source_validated_ds1302_wiring_code_safety_and_references(self):
        page = ROOT / "web" / "lessons" / "19-a-clock-that-never-forgets.html"
        self.assertTrue(page.exists(), "Lesson 19 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "A Clock That Never Forgets",
            "Arduino 5V → DS1302 VCC",
            "Arduino GND → DS1302 GND",
            "Arduino D2 → DS1302 CLK",
            "Arduino D3 → DS1302 DAT",
            "Arduino D4 → DS1302 RST/CE",
            "#define DS1302_CLK_PIN 2",
            "#define DS1302_IO_PIN 3",
            "#define DS1302_CE_PIN 4",
            "ErriezDS1302 rtc(DS1302_CLK_PIN, DS1302_IO_PIN, DS1302_CE_PIN);",
            "rtc.setDateTime(12, 34, 56, 31, 12, 2020, 0)",
            "rtc.getDateTime(&hour, &minute, &second, &day, &month, &year, &weekday)",
            "not compatible with SPI",
            "more than one minute each day",
            "Reference pages",
            "ErriezDS1302",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-19" / "lesson-19-erriez-ds1302-module.png"
        self.assertTrue(asset.is_file(), "Lesson 19 reference image is missing")
        page = (ROOT / "web" / "lessons" / "19-a-clock-that-never-forgets.html").read_text(encoding="utf-8")
        self.assertIn("Erriez", page)
        self.assertIn("MIT", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("19-a-clock-that-never-forgets.html", index)


if __name__ == "__main__":
    unittest.main()
