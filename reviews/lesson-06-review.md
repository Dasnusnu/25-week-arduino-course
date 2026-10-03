# Lesson 06 review — Mix Your Own Colours

**Status:** PASS — ready for independent review

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/06-mix-your-own-colours.html`
- Curriculum-card link: `web/app.js`
- Per-lesson checklist storage: `web/lesson.js`
- Reference image: `web/assets/lesson-06/lesson-06-rgb-circuit.jpg`
- Focused contract test: `tests/test_lesson_06.py`

## Reference validation

Primary reference: `sources/freenove-ultimate-starter-kit/Tutorial.pdf`, Chapter 8, Project 8.1 “Control RGB LED through Potentiometer,” PDF pages 78–81 / printed pages 74–77. The checked upstream public page is [Freenove Chapter 8: RGB LED](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/8_RGB.html). The local reference sketch is `sources/freenove-ultimate-starter-kit/Sketches/Sketch_8.1.1_Control_RGB_LED_through_Potentiometer/Sketch_8.1.1_Control_RGB_LED_through_Potentiometer.ino`, lines 9–30.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| The build uses an RGB LED, three 220 Ω resistors, three potentiometers, a breadboard, USB-connected board, and jumper wires | Project 8.1 component list, printed page 74; official component-list section | Pass |
| The potentiometer wipers are read at A0, A1, and A2 | Project 8.1 schematic/hardware connection, PDF page 80 / printed page 76; official circuit section | Pass |
| PWM connections are pin 11 → red, pin 10 → green, and pin 9 → blue, each through a 220 Ω resistor | Project 8.1 schematic, PDF page 80 / printed page 76; official circuit section and sketch lines 9–11 | Pass |
| The illustrated RGB LED common terminal connects to 5 V | Project 8.1 schematic, PDF page 80 / printed page 76 | Pass |
| The three inputs are converted from 0–1023 ADC values to 0–255 PWM values | Local reference sketch lines 21–30; official Sketch 8.1.1 | Pass |
| The lesson uses `255 - channel` for this 5 V common (common-anode) circuit | Electrical interpretation of the source schematic: a channel shines when its Arduino output is driven low; original lesson code makes that inversion explicit | Pass |

The official prose labels the long common lead “Cathode (+)” and the three channel leads “Anodes (-),” which conflicts with standard diode terminology. The source schematic visibly connects the common terminal to 5 V. The lesson therefore calls this wiring common-anode, warns against using it with common-cathode RGB LEDs, and bases the PWM inversion on the schematic rather than repeating the contradictory labels.

## Attribution and source handling

- The lesson includes an unchanged rasterization of the permitted source-pack PDF page containing the Project 8.1 schematic and hardware connection, with visible Chapter/page attribution.
- The page names Freenove, links the direct official Chapter 8 page and tutorial index under the required `Reference pages` heading, and links CC BY-NC-SA 3.0.
- The source pack was not modified. No generated image or third-party source pack was added.

## Interactive verification

- Red test first: `python -m unittest tests/test_lesson_06.py -v` → **2 failures** before the lesson page and curriculum-card link existed, as expected.
- Focused static contract test: `python -m unittest tests/test_lesson_06.py -v` → **2 passed**.
- Full static test suite: `python -m unittest discover -s tests -v` → **12 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- JPEG verification: Pillow opened and verified `lesson-06-rgb-circuit.jpg` at **1075 × 1521**.
- Browser test using the local Week 06 lesson file:
  - the reference image loaded successfully (`complete: true`, natural size 1075 × 1521);
  - five checklist controls rendered and initial progress read 0 of 5;
  - a real visible checkbox click updated progress to 1 of 5 and stored `["1"]` under the lesson-specific key;
  - reset returned progress to 0 of 5, cleared all controls, and stored `[]`;
  - the `Reference pages` section rendered with the direct official Chapter 8 and tutorial-index links.

## Limitations

This review validates the lesson against Freenove’s reference materials and browser behavior. It does **not** electrically test a physical Uno-compatible board, RGB LED type, potentiometers, resistor values, or the colour-channel order; confirm the target kit’s LED markings and source layout before applying USB power. The curriculum index uses `fetch`, so its cards are designed for a web-served preview rather than direct `file://` loading.
