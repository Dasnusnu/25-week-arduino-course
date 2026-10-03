# Lesson 03 review — The Melody Machine

**Status:** PASS — ready for independent review

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/03-the-melody-machine.html`
- Curriculum-card link: `web/app.js`
- Per-lesson checklist storage: `web/lesson.js`
- Reference image: `web/assets/lesson-03/lesson-03-passive-buzzer-circuit.jpg`
- Focused contract test: `tests/test_lesson_03.py`

## Reference validation

Primary reference: `sources/freenove-ultimate-starter-kit/Tutorial.pdf`, Chapter 9, Project 9.2 “Passive Buzzer,” PDF page 92 / printed page 88–89. The checked upstream public page is [Freenove Chapter 9: Buzzer](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/9_Buzzer.html).

| Lesson claim | Reference evidence | Result |
|---|---|---|
| The build uses a board, breadboard, USB cable, passive buzzer, NPN transistor, 1 × 1 kΩ resistor, and four jumpers | Project 9.2 component list, printed page 87 | Pass |
| Pin 9 drives the passive-buzzer circuit through the source NPN transistor circuit | Project 9.2 circuit, printed page 88; upstream Project Passive Buzzer circuit section | Pass |
| The passive buzzer needs an externally changing signal, unlike an active buzzer | Chapter 9 buzzer explanation | Pass |
| The source sketch uses `tone()` on pin 9 while its frequency follows `2000 + sin(...) * 500`, spanning approximately 1500–2500 Hz | Project 9.2 sketch, printed page 89; local `Sketches/Sketch_9.2.1_Passive_Buzzer/Sketch_9.2.1_Passive_Buzzer.ino`, lines 9–24 | Pass |
| The original lesson sketch preserves the source behavior with clear new names: pin 9 output, degree-to-radian conversion, a 2000 Hz center, a 500 Hz sweep, `tone()`, and a 1 ms update | Lesson source review against the local reference sketch | Pass |

## Attribution and source handling

- The lesson includes an unchanged rasterization of the permitted source-pack PDF page containing the Project 9.2 schematic, hardware connection, and frequency graph, with visible Chapter/page attribution.
- The page names Freenove, links the direct official Chapter 9 page and tutorial index under the required `Reference pages` heading, and links CC BY-NC-SA 3.0.
- The source pack was not modified. No generated image or third-party source pack was added.

## Interactive verification

- Red test first: `python -m unittest tests/test_lesson_03.py -v` → **2 failures** before the lesson page and reference image existed, as expected.
- Focused static contract test: `python -m unittest tests/test_lesson_03.py -v` → **2 passed**.
- Full static test suite: `python -m unittest discover -s tests -v` → **6 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test using the local Week 03 lesson file:
  - the 910 × 1287 JPEG reference image loaded successfully;
  - five checklist controls rendered and initial progress read 0 of 5;
  - a real checkbox click updated progress to 1 of 5 and stored `["1"]` under the lesson-specific key;
  - reset returned progress to 0 of 5, cleared all controls, and stored `[]`;
  - the `Reference pages` section rendered with direct official Chapter 9 and tutorial-index links.

## Limitations

This review validates the lesson against Freenove’s reference materials and browser behavior. It does **not** electrically test a physical board, transistor, or passive buzzer; a final hardware check must use the target Uno-compatible kit and the shown transistor orientation and buzzer polarity.
