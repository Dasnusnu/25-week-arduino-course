from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson01ContractTest(unittest.TestCase):
    def test_lesson_page_has_progressive_build_and_reference_image(self):
        page = ROOT / "web" / "lessons" / "01-light-your-first-led.html"
        self.assertTrue(page.exists(), "Lesson 01 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "Step 1",
            "Step 2",
            "Step 3",
            "Check your work",
            "Freenove Ultimate Starter Kit",
            "lesson-01-components.jpg",
            "lesson-01-wiring.jpg",
        ):
            self.assertIn(required, content)

    def test_lesson_reference_assets_are_present(self):
        assets = ROOT / "web" / "assets" / "lesson-01"
        self.assertTrue((assets / "lesson-01-components.jpg").is_file())
        self.assertTrue((assets / "lesson-01-wiring.jpg").is_file())


if __name__ == "__main__":
    unittest.main()
