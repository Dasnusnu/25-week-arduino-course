from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson04ContractTest(unittest.TestCase):
    def test_lesson_page_has_potentiometer_adc_build_and_references(self):
        page = ROOT / "web" / "lessons" / "04-the-control-knob.html"
        self.assertTrue(page.exists(), "Lesson 04 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Control Knob",
            "rotary potentiometer",
            "A0",
            "5 V",
            "GND",
            "analogRead(A0)",
            "5.0 / 1023.0",
            "Serial.begin(9600)",
            "Reference pages",
            "7_ADC.html",
            "lesson-04-adc-circuit.jpg",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_reference_asset_and_interactive_link_are_present(self):
        asset = ROOT / "web" / "assets" / "lesson-04" / "lesson-04-adc-circuit.jpg"
        self.assertTrue(asset.is_file(), "Lesson 04 reference image is missing")
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("04-the-control-knob.html", index)


if __name__ == "__main__":
    unittest.main()
