# Lesson 02 review — Make Some Noise

**Status:** PASS — ready for independent review

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/02-make-some-noise.html`
- Curriculum-card link: `web/app.js`
- Per-lesson checklist storage: `web/lesson.js`
- Reference image: `web/assets/lesson-02/lesson-02-active-buzzer-circuit.jpg`
- Focused contract test: `tests/test_lesson_02.py`

## Reference validation

Primary reference: `sources/freenove-ultimate-starter-kit/Tutorial.pdf`, Chapter 9, Project 9.1 “Active Buzzer,” PDF page 89 / printed page 85. The checked upstream public page is [Freenove Chapter 9: Buzzer](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/9_Buzzer.html).

| Lesson claim | Reference evidence | Result |
|---|---|---|
| The build uses an active buzzer, NPN transistor, push button, 1 × 1 kΩ resistor, 2 × 10 kΩ resistors, board, breadboard, USB cable, and six jumpers | Chapter 9 Project 9.1 component list | Pass |
| Pin 12 reads the push-button state and pin 9 drives the active buzzer circuit | Tutorial PDF printed page 85; upstream Chapter 9 circuit section | Pass |
| The button is unpressed at HIGH and pressed at LOW | Sketch 9.1.1 and the button pull-up / grounded-switch schematic | Pass |
| Pin 9’s HIGH level drives the NPN transistor so the active buzzer sounds while the button is pressed | Sketch 9.1.1 and Chapter 9 transistor explanation | Pass |
| Lesson code configures pin 12 as `INPUT`, pin 9 as `OUTPUT`, and performs the same tested low-pressed/high-buzzer behavior with original variable names and layout | Local source sketch `Sketches/Sketch_9.1.1_Active_Buzzer/Sketch_9.1.1_Active_Buzzer.ino`, lines 9–22 | Pass |

## Attribution and source handling

- The lesson includes the prepared, unchanged source-page image beside the build steps with its Chapter 9 / page attribution.
- The page names Freenove, links the exact official Chapter 9 page and tutorial index under the required `Reference pages` heading, and links the source’s CC BY-NC-SA 3.0 license.
- The source pack itself was not modified or included as a newly downloaded third-party pack.

## Interactive verification

- Red test first: `python3 -m unittest tests/test_lesson_02.py` → **2 failures** before the lesson page and image existed, as expected.
- Focused static contract test: `python3 -m unittest tests/test_lesson_02.py` → **2 passed**.
- Full static test suite: `python3 -m unittest discover -s tests` → **4 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test using the local lesson file:
  - the 910 × 1287 JPEG reference image loaded successfully;
  - five checklist controls rendered and initial progress read 0/5;
  - a real checkbox click updated progress to 1/5 and stored `["1"]` under the lesson-specific key;
  - reset returned progress to 0/5, cleared all controls, and stored `[]`;
  - the Reference pages section rendered with the direct Chapter 9 and tutorial-index links.

## Limitations

This review validates the lesson against Freenove’s reference material and browser behavior. It does **not** electrically test a physical board, transistor, button, or buzzer; a final hardware check must use the target Uno-compatible kit and the shown transistor orientation.
