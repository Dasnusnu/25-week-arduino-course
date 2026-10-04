from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson20ContractTest(unittest.TestCase):
    def test_lesson_page_has_source_validated_ir_wiring_code_safety_and_references(self):
        page = ROOT / "web" / "lessons" / "20-control-it-by-remote.html"
        self.assertTrue(page.exists(), "Lesson 20 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "Control It by Remote",
            "Arduino 5 V → IR receiver VCC",
            "Arduino GND → IR receiver GND",
            "Arduino D12 → IR receiver DATA",
            "10 kΩ pull-up resistor",
            "const byte receivePin = 12;",
            "IrReceiver.begin(receivePin, ENABLE_LED_FEEDBACK);",
            "if (IrReceiver.decode())",
            "IrReceiver.decodedIRData.decodedRawData",
            "IrReceiver.resume();",
            "Serial.begin(9600);",
            "do not assume a three-pin receiver has the same pin order",
            "Reference pages",
            "21_Infrared_Remote.html",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-20" / "lesson-20-freenove-ir-receiver-circuit.png"
        self.assertTrue(asset.is_file(), "Lesson 20 reference image is missing")
        page = (ROOT / "web" / "lessons" / "20-control-it-by-remote.html").read_text(encoding="utf-8")
        self.assertIn("Freenove", page)
        self.assertIn("CC BY-NC-SA 3.0", page)
        self.assertIn("Project 21.1", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("20-control-it-by-remote.html", index)


if __name__ == "__main__":
    unittest.main()
