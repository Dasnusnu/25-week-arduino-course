from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Lesson21ContractTest(unittest.TestCase):
    def test_lesson_page_has_source_validated_remote_lamp_wiring_code_safety_and_references(self):
        page = ROOT / "web" / "lessons" / "21-the-remote-controlled-lamp.html"
        self.assertTrue(page.exists(), "Lesson 21 page is missing")
        content = page.read_text(encoding="utf-8")
        for required in (
            "The Remote-Controlled Lamp",
            "Arduino 5 V → IR receiver VCC",
            "Arduino GND → IR receiver GND",
            "Arduino D12 → IR receiver DATA",
            "Arduino D5 → LED anode",
            "LED cathode → 220 Ω resistor → Arduino GND",
            "10 kΩ pull-up resistor",
            "const byte receivePin = 12;",
            "const byte lampPin = 5;",
            "IrReceiver.begin(receivePin, ENABLE_LED_FEEDBACK);",
            "IrReceiver.decodedIRData.command",
            "IRDATA_FLAGS_IS_REPEAT",
            "analogWrite(lampPin, 255);",
            "analogWrite(lampPin, 0);",
            "AC mains",
            "Reference pages",
            "21_Infrared_Remote.html",
            "data-step=\"5\"",
        ):
            self.assertIn(required, content)

    def test_lesson_has_attributed_local_reference_image_and_is_linked(self):
        asset = ROOT / "web" / "assets" / "lesson-21" / "lesson-21-freenove-remote-led-circuit.png"
        self.assertTrue(asset.is_file(), "Lesson 21 reference image is missing")
        page = (ROOT / "web" / "lessons" / "21-the-remote-controlled-lamp.html").read_text(encoding="utf-8")
        self.assertIn("Freenove", page)
        self.assertIn("CC BY-NC-SA 3.0", page)
        self.assertIn("Project 21.2", page)
        self.assertIn("unchanged", page)
        index = (ROOT / "web" / "app.js").read_text(encoding="utf-8")
        self.assertIn("21-the-remote-controlled-lamp.html", index)


if __name__ == "__main__":
    unittest.main()
