from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson10ContractTest(unittest.TestCase):
    def test_lesson_page_has_capacitive_build_code_and_references(self):
        page = ROOT / "web" / "lessons" / "10-the-water-detector.html"
        self.assertTrue(page.exists(), "Lesson 10 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Water Detector",
            "10 MΩ resistor",
            "digital pin 2",
            "digital pin 3",
            "aluminum foil",
            "RBD::WaterSensor water_sensor(2, 3, 3)",
            "Serial.begin(115200)",
            "water_sensor.update()",
            "water_sensor.onRawValueChange()",
            "water_sensor.getActiveLevel()",
            "water_sensor.getRawValue()",
            "Reference pages",
            "docs-arduino-water-sensor.html",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_images_and_is_linked(self):
        page = ROOT / "web" / "lessons" / "10-the-water-detector.html"
        content = page.read_text(encoding="utf-8")
        for asset_name in (
            "lesson-10-keyestudio-water-level-sensor.png",
            "lesson-10-keyestudio-water-level-alarm-circuit.png",
        ):
            self.assertTrue(
                (ROOT / "web" / "assets" / "lesson-10" / asset_name).is_file(),
                f"Lesson 10 reference image is missing: {asset_name}",
            )
            self.assertIn(asset_name, content)
        self.assertIn("Keyestudio", content)
        self.assertIn("Project 10 Water Level Alarm", content)
        self.assertIn("Project10.html", content)
        self.assertIn("not this lesson’s dry RBD foil-and-cup capacitive sensor", content)
        self.assertIn('class="wiring-map"', content)
        self.assertIn('role="img"', content)
        self.assertIn('Wiring map: original text rendering', content)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("10-the-water-detector.html", index)


if __name__ == "__main__":
    unittest.main()
