# Lesson 05 review — The Darkness Detector

**Status:** PASS — ready for independent review

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/05-the-darkness-detector.html`
- Curriculum-card link: `web/app.js`
- Curriculum source coverage: `data/lessons.json`
- Per-lesson checklist storage: `web/lesson.js`
- Reference image: `web/assets/lesson-05/lesson-05-photoresistor-circuit.jpg`
- Focused contract test: `tests/test_lesson_05.py`

## Reference validation

Primary reference: `sources/freenove-ultimate-starter-kit/Tutorial.pdf`, Chapter 7, Project 7.3 “Control LED by Potentiometer” (the source project’s heading; its described sensor is a photoresistor), PDF pages 74–77 / printed pages 70–73. The checked upstream public page is [Freenove Chapter 7: ADC](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/7_ADC.html). The local reference sketch is `sources/freenove-ultimate-starter-kit/Sketches/Sketch_7.3.1_Control_LED_through_Photoresistor/Sketch_7.3.1_Control_LED_through_Photoresistor.ino`, lines 9–20.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| The build uses a board, breadboard, USB cable, photoresistor, LED, 10 kΩ resistor, 220 Ω resistor, and five jumper wires | Project 7.3 component list, printed page 70; upstream component-list section | Pass |
| A 10 kΩ resistor runs from 5 V to the A0 junction, and the photoresistor runs from that junction to GND | Project 7.3 schematic and hardware connection, PDF page 76 / printed page 72; upstream circuit and photoresistor sections | Pass |
| LED control uses pin 9 and a 220 Ω series resistor, with the LED returning to GND | Project 7.3 schematic, PDF page 76 / printed page 72; upstream circuit section | Pass |
| The photoresistor resistance drops in brighter light; its divider junction voltage is read at A0 | Project 7.3 photoresistor explanation, printed page 71; upstream photoresistor section | Pass |
| The sketch reads A0 and maps 0–1023 to PWM 0–255 on pin 9 | Local reference sketch lines 9–20; upstream Sketch 7.3.1 | Pass |
| The original lesson adds a 50 ms delay only to make observation calmer; its sensing and PWM mapping remain source-equivalent | Lesson source review against the local reference sketch | Pass |

## Attribution and source handling

- The lesson includes an unchanged rasterization of the permitted source-pack PDF page containing the Project 7.3 schematic and hardware connection, with visible Chapter/page attribution.
- The page names Freenove, links the direct official Chapter 7 page and tutorial index under the required `Reference pages` heading, and links CC BY-NC-SA 3.0.
- The source pack was not modified. No generated image or third-party source pack was added.

## Interactive verification

- Red test first: `python -m unittest tests/test_lesson_05.py -v` → **2 failures** before the lesson page and reference image existed, as expected.
- Focused static contract test: `python -m unittest tests/test_lesson_05.py -v` → **2 passed**.
- Full static test suite: `python -m unittest discover -s tests -v` → **10 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- JPEG verification: Pillow opened and verified `lesson-05-photoresistor-circuit.jpg` at **1241 × 1754**.
- Browser test using the local Week 05 lesson file:
  - the reference image loaded successfully (`complete: true`, natural size 1241 × 1754);
  - five checklist controls rendered and initial progress read 0 of 5;
  - a real visible checkbox click updated progress to 1 of 5 and stored `["1"]` under the lesson-specific key;
  - reset returned progress to 0 of 5, cleared all controls, and stored `[]`;
  - the `Reference pages` section rendered with direct official Chapter 7 and tutorial-index links.

## Limitations

This review validates the lesson against Freenove’s reference materials and browser behavior. It does **not** electrically test a physical Uno-compatible board, photoresistor, LED, or resistor values; a final hardware check must use the target kit and confirm the shown LED orientation and breadboard rows before power is connected.
