from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson14ContractTest(unittest.TestCase):
    def test_lesson_page_has_ky038_clap_build_code_and_references(self):
        page = ROOT / "web" / "lessons" / "14-the-clap-trigger.html"
        self.assertTrue(page.exists(), "Lesson 14 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Clap Trigger",
            "KY-038",
            "VCC → Arduino 5V",
            "GND → Arduino GND",
            "DO → Arduino D9",
            "digitalRead(soundPin)",
            "const unsigned long lockoutMs = 350",
            "Reference pages",
            "luisllamas.es/en/detect-sound-arduino-ky-038-microphone",
            "CC BY-NC-SA",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-14" / "lesson-14-ky038-wiring.webp"
        self.assertTrue(asset.is_file(), "Lesson 14 reference image is missing")
        page = (ROOT / "web" / "lessons" / "14-the-clap-trigger.html").read_text(encoding="utf-8")
        self.assertIn("Luis Llamas", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("14-the-clap-trigger.html", index)
        inventory = (ROOT / "data" / "lessons.json").read_text(encoding="utf-8")
        self.assertIn('"week":14', inventory)
        self.assertIn('"covered":true', inventory)


if __name__ == "__main__":
    unittest.main()
