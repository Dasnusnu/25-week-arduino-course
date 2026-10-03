from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson09ContractTest(unittest.TestCase):
    def test_lesson_page_has_dht11_build_code_and_references(self):
        page = ROOT / "web" / "lessons" / "09-the-room-thermometer.html"
        self.assertTrue(page.exists(), "Lesson 09 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Room Thermometer",
            "DHT11",
            "10 kΩ",
            "Arduino pin 10",
            "#include &lt;dht.h&gt;",
            "int dhtPin = 10",
            "DHT.read11(dhtPin)",
            "Serial.begin(9600)",
            "DHTLIB_OK",
            "DHTLIB_ERROR_CHECKSUM",
            "DHTLIB_ERROR_TIMEOUT",
            "delay(1000)",
            "Reference pages",
            "22_Temperature%26Humidity.html",
            "lesson-09-dht11-hardware-connection.jpg",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_reference_asset_and_interactive_link_are_present(self):
        asset = ROOT / "web" / "assets" / "lesson-09" / "lesson-09-dht11-hardware-connection.jpg"
        self.assertTrue(asset.is_file(), "Lesson 09 reference image is missing")
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("09-the-room-thermometer.html", index)


if __name__ == "__main__":
    unittest.main()
