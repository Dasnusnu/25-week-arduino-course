from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson05ContractTest(unittest.TestCase):
    def test_lesson_page_has_photoresistor_darkness_build_and_references(self):
        page = ROOT / "web" / "lessons" / "05-the-darkness-detector.html"
        self.assertTrue(page.exists(), "Lesson 05 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Darkness Detector",
            "photoresistor",
            "10 kΩ",
            "220 Ω",
            "A0",
            "pin 9",
            "analogRead(lightPin)",
            "analogWrite(ledPin, map(rawLight, 0, 1023, 0, 255))",
            "Reference pages",
            "7_ADC.html",
            "lesson-05-photoresistor-circuit.jpg",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_reference_asset_and_interactive_link_are_present(self):
        asset = ROOT / "web" / "assets" / "lesson-05" / "lesson-05-photoresistor-circuit.jpg"
        self.assertTrue(asset.is_file(), "Lesson 05 reference image is missing")
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("05-the-darkness-detector.html", index)


if __name__ == "__main__":
    unittest.main()
