# Lesson 07 review — Make Numbers Appear

**Status:** PASS — ready for independent review

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/07-make-numbers-appear.html`
- Curriculum-card link: `web/app.js`
- Per-lesson checklist storage: `web/lesson.js`
- Reference image: `web/assets/lesson-07/lesson-07-seven-segment-circuit.jpg`
- Focused contract test: `tests/test_lesson_07.py`

## Reference validation

Primary reference: `sources/freenove-ultimate-starter-kit/Tutorial.pdf`, Chapter 17, Project 17.1 “1-digit 7-segment Display,” PDF pages 157–161 / printed pages 153–157. The checked upstream public page is [Freenove Chapter 17: Digital Display](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/17_Digital_Display.html). The local reference sketch is `sources/freenove-ultimate-starter-kit/Sketches/Sketch_17.1.1_1_Digit_7_Segment_Display/Sketch_17.1.1_1_Digit_7_Segment_Display.ino`, lines 9–33.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| The project uses a board, USB cable, breadboard, 74HC595, one-digit 7-segment display, eight 220 Ω resistors, and 18 jumpers | Project 17.1 component list, PDF page 157 / printed page 153; official component-list section | Pass |
| The 1-digit display is common-anode and has individual cathode paths | Project 17.1 component-knowledge text and display diagram, PDF page 158 / printed page 154; official component-knowledge section | Pass |
| Arduino pin 11 goes to DS (74HC595 pin 14), pin 13 to SH_CP (pin 11), and pin 12 to ST_CP (pin 12) | Project 17.1 schematic, PDF page 159 / printed page 155; local sketch lines 9–11 | Pass |
| The shift-register power/control connections are VCC pin 16 and MR pin 10 to 5 V, plus GND pin 8 and OE pin 13 to GND | Project 17.1 schematic, PDF page 159 / printed page 155 | Pass |
| Each Q0–Q7 output reaches an individual display LED path through its own 220 Ω resistor | Project 17.1 schematic, PDF page 159 / printed page 155 | Pass |
| Common-anode digit patterns for 0–9 are `0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90` | Local sketch line 14; official sketch section | Pass |
| The lesson latches low, uses `shiftOut(..., MSBFIRST, digits[i])`, latches high, and waits one second | Local sketch lines 23–33; original lesson narrows its first loop to digits 0–9 rather than source 0–F | Pass |

## Attribution and source handling

- The lesson includes an unchanged rasterization of the permitted source-pack PDF page containing Project 17.1’s schematic and hardware connection, with visible Chapter/page attribution.
- The page names Freenove, links the direct official Chapter 17 page and tutorial index under the required `Reference pages` heading, and links CC BY-NC-SA 3.0.
- The source pack was not modified. No generated image or third-party source pack was added.

## Interactive verification

- Red test first: `python -m unittest tests/test_lesson_07.py -v` → **2 failures** before the page and image existed, as expected.
- Focused static contract test: `python -m unittest tests/test_lesson_07.py -v` → **2 passed**.
- Full static test suite: `python -m unittest discover -s tests -v` → **14 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- JPEG verification: Pillow opened and verified `lesson-07-seven-segment-circuit.jpg` at **1241 × 1754**.
- Browser test using the local Week 07 lesson file:
  - the reference image loaded successfully (`complete: true`, natural size 1241 × 1754);
  - five checklist controls rendered and initial progress read 0 of 5;
  - a real visible checkbox click updated progress to 1 of 5 and stored `["1"]` under the lesson-specific key;
  - a real visible reset-button click returned progress to 0 of 5, cleared all controls, and stored `[]`;
  - the `Reference pages` section rendered with direct official Chapter 17 and tutorial-index links.

## Limitations

This review validates the lesson against Freenove’s reference materials and browser behavior. It does **not** electrically test a physical Uno-compatible board, 74HC595, display pinout/type, resistor values, or uploaded sketch. Before USB power is connected, verify the target kit’s display pin designations and every breadboard row against the source image.
