from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson03ContractTest(unittest.TestCase):
    def test_lesson_page_has_passive_buzzer_build_and_references(self):
        page = ROOT / "web" / "lessons" / "03-the-melody-machine.html"
        self.assertTrue(page.exists(), "Lesson 03 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Melody Machine",
            "passive buzzer",
            "pin 9",
            "NPN transistor",
            "1 kΩ",
            "2000",
            "sin(",
            "tone(buzzerPin, toneVal)",
            "Reference pages",
            "9_Buzzer.html",
            "lesson-03-passive-buzzer-circuit.jpg",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_reference_asset_and_interactive_link_are_present(self):
        asset = ROOT / "web" / "assets" / "lesson-03" / "lesson-03-passive-buzzer-circuit.jpg"
        self.assertTrue(asset.is_file(), "Lesson 03 reference image is missing")
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("03-the-melody-machine.html", index)


if __name__ == "__main__":
    unittest.main()
