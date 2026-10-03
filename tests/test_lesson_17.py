from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson17ContractTest(unittest.TestCase):
    def test_lesson_page_has_source_validated_stepper_wiring_code_safety_and_references(self):
        page = ROOT / "web" / "lessons" / "17-the-precision-spinner.html"
        self.assertTrue(page.exists(), "Lesson 17 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Precision Spinner",
            "ULN2003",
            "pins 11, 10, 9, and 8",
            "IN1",
            "IN2",
            "IN3",
            "IN4",
            "32 × 64 = 2048",
            "Never connect the motor or driver directly to an Arduino pin",
            "const byte outPorts[] = {11, 10, 9, 8};",
            "moveSteps(true, stepsPerTurn, stepDelayMs);",
            "moveSteps(false, stepsPerTurn, stepDelayMs);",
            "Reference pages",
            "18_Stepper_Motor.html",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-17" / "lesson-17-freenove-stepper-circuit.png"
        self.assertTrue(asset.is_file(), "Lesson 17 reference image is missing")
        page = (ROOT / "web" / "lessons" / "17-the-precision-spinner.html").read_text(encoding="utf-8")
        self.assertIn("Freenove", page)
        self.assertIn("CC BY-NC-SA 3.0", page)
        self.assertIn("Project 18.1", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("17-the-precision-spinner.html", index)


if __name__ == "__main__":
    unittest.main()
