# Lesson 04 review — The Control Knob

**Status:** PASS — ready for independent review

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/04-the-control-knob.html`
- Curriculum-card link: `web/app.js`
- Per-lesson checklist storage: `web/lesson.js`
- Reference image: `web/assets/lesson-04/lesson-04-adc-circuit.jpg`
- Focused contract test: `tests/test_lesson_04.py`

## Reference validation

Primary reference: `sources/freenove-ultimate-starter-kit/Tutorial.pdf`, Chapter 7, Project 7.1 “ADC,” PDF pages 66–70 / printed pages 62–66. The checked upstream public page is [Freenove Chapter 7: ADC](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/7_ADC.html). The local reference sketch is `sources/freenove-ultimate-starter-kit/Sketches/Sketch_7.1.1_ADC/Sketch_7.1.1_ADC.ino`, lines 9–25.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| The build uses a board, breadboard, USB cable, rotary potentiometer, and three jumper wires | Project 7.1 component list, printed page 62; upstream component-list section | Pass |
| The rotary potentiometer connects terminal 1 to 5 V, terminal 2 to GND, and its middle wiper/terminal 3 to A0 | Project 7.1 circuit schematic and hardware connection, printed page 65; upstream circuit section | Pass |
| A0 measures the potentiometer voltage and the Uno ADC has 10-bit resolution, producing 0–1023 readings | Project 7.1 ADC explanation and circuit, printed pages 63 and 65; upstream ADC and circuit sections | Pass |
| The source sketch starts Serial at 9600, reads `analogRead(A0)`, calculates voltage with `5.0 / 1023.0`, and updates every 500 ms | Project 7.1 sketch, printed page 66; local reference sketch lines 12–25 | Pass |
| The original lesson sketch preserves that behavior with new learner-facing labels and two-decimal Serial output | Lesson source review against the local reference sketch | Pass |

## Attribution and source handling

- The lesson includes an unchanged rasterization of the permitted source-pack PDF page containing the Project 7.1 schematic and hardware connection, with visible Chapter/page attribution.
- The page names Freenove, links the direct official Chapter 7 page and tutorial index under the required `Reference pages` heading, and links CC BY-NC-SA 3.0.
- The source pack was not modified. No generated image or third-party source pack was added.

## Interactive verification

- Red test first: `python -m unittest tests/test_lesson_04.py -v` → **2 failures** before the lesson page and reference image existed, as expected.
- Focused static contract test: `python -m unittest tests/test_lesson_04.py -v` → **2 passed**.
- Full static test suite: `python -m unittest discover -s tests -v` → **8 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- JPEG verification: Pillow opened and verified `lesson-04-adc-circuit.jpg` at **1191 × 1684**.
- Browser test using the local Week 04 lesson file:
  - the reference image loaded successfully (`complete: true`, natural size 1191 × 1684);
  - five checklist controls rendered and initial progress read 0 of 5;
  - a real visible checkbox click updated progress to 1 of 5 and stored `["1"]` under the lesson-specific key;
  - reset returned progress to 0 of 5, cleared all controls, and stored `[]`;
  - the `Reference pages` section rendered with direct official Chapter 7 and tutorial-index links.

## Limitations

This review validates the lesson against Freenove’s reference materials and browser behavior. It does **not** electrically test a physical Uno-compatible board or potentiometer; a final hardware check must use the target kit and confirm the shown terminal placement before power is connected.
