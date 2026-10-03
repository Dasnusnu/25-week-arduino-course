from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson12ContractTest(unittest.TestCase):
    def test_lesson_page_has_keypad_lock_build_code_and_references(self):
        page = ROOT / "web" / "lessons" / "12-the-secret-password-pad.html"
        self.assertTrue(page.exists(), "Lesson 12 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Secret Password Pad",
            "4×4 keypad",
            "keypad pin 8 → Arduino D11",
            "keypad pin 1 → Arduino D4",
            "Arduino D13",
            "1 kΩ resistor",
            "Arduino D12",
            "#include &lt;Keypad.h&gt;",
            "#include &lt;Servo.h&gt;",
            "byte rowPins[4] = {11, 10, 9, 8}",
            "byte colPins[4] = {7, 6, 5, 4}",
            "const char secret[] = \"2580\"",
            "keypad.getKey()",
            "lockServo.write(135)",
            "lockServo.write(45)",
            "Reference pages",
            "19_Matrix_Keypad.html",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-12" / "lesson-12-freenove-combination-lock-circuit.png"
        self.assertTrue(asset.is_file(), "Lesson 12 reference image is missing")
        page = (ROOT / "web" / "lessons" / "12-the-secret-password-pad.html").read_text(encoding="utf-8")
        self.assertIn("Freenove", page)
        self.assertIn("CC BY-NC-SA 3.0", page)
        self.assertIn("Project 19.2", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("12-the-secret-password-pad.html", index)


if __name__ == "__main__":
    unittest.main()
