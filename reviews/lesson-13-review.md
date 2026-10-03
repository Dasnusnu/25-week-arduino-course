# Lesson 13 review — The Game-Style Joystick

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/13-the-game-style-joystick.html`
- Local reference asset: `web/assets/lesson-13/lesson-13-freenove-joystick-circuit.png`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_13.py`

## Reference validation

Primary retained source: `sources/freenove-ultimate-starter-kit/`, exact upstream revision `5315f61497eea49553aa1b70721751fb16a497e5`, under CC BY-NC-SA 3.0 as recorded in `SOURCES.md`. Source sketch checked: `Sketches/Sketch_13.1.1_Joystick/Sketch_13.1.1_Joystick.ino`, lines 9–33. The public primary reference checked was [Freenove Chapter 13 — Joystick](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/13_Joystick.html). ADC range guidance was checked against [Arduino analogRead() documentation](https://docs.arduino.cc/language-reference/en/functions/analog-io/analogRead/).

| Lesson claim | Reference evidence | Result |
|---|---|---|
| A joystick supplies two analog axes and a press switch | Freenove Chapter 13 component knowledge | Pass |
| GND and +5V power the module; VRx routes to A0, VRy to A1, and SW to D8 | Freenove Chapter 13 circuit and retained source PDF printed page 116 / PDF page 120 | Pass |
| The switch uses `INPUT_PULLUP`, is HIGH at rest, and reads LOW when pressed | Freenove Chapter 13 explanation and retained sketch lines 14–16, 24–25 | Pass |
| The source samples both analog pins and switch, writes serial output at 9600 baud, and waits 200 ms | Retained sketch lines 16, 20–33 and public Chapter 13 page | Pass |
| Classic Uno `analogRead()` values are 10-bit values from 0 through 1023 | Arduino `analogRead()` documentation | Pass |
| Center calibration plus an 80-count dead zone avoids tiny resting changes being labeled as directions | Original lesson behavior; safely built on source-validated readings, not presented as Freenove source behavior | Pass, clearly scoped |

The learner sketch is original: it uses named `A0`/`A1` pins, captures the resting position at startup, adds a configurable dead zone, and prints direction labels. It retains the source-validated wiring, pull-up switch logic, 9600-baud serial communication, and 200 ms sampling. The page links actual public technical references in a section titled exactly **Reference pages**.

## Attribution and image handling

- `lesson-13-freenove-joystick-circuit.png` is a non-generated, unchanged PNG extraction of Freenove’s `Tutorial.pdf`, Chapter 13 Project 13.1 circuit page (printed page 116 / PDF page 120).
- The image was inspected after export and is a valid 1241 × 1754 PNG. It visibly shows the labeled GND, +5V, VRX, VRY, SW, A0, A1, and Pin 8 paths.
- Its figure caption visibly attributes Freenove; identifies Chapter 13, Project 13.1, printed/PDF pages; identifies the page as unchanged; links CC BY-NC-SA 3.0; and points to the bottom reference section.
- Freenove’s upstream repository declares all repository files CC BY-NC-SA 3.0. This project is original and noncommercial; attribution and share-alike conditions remain visible. `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_13.py -v` initially failed as expected because the Week 13 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_13.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **26 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/13-the-game-style-joystick.html`:
  - heading rendered as “The Game-Style Joystick”; the local Freenove image loaded (`complete: true`, natural size `1241 × 1754`); and the “Reference pages” heading rendered;
  - five checklist controls rendered at `0 of 5 checks complete.`;
  - a visible click on the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and stored `["1"]`;
  - a visible click on `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]` under the lesson’s local-storage key.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, a particular joystick module’s label order or axis orientation, USB power, any wiring, Serial Monitor, upload, or observed values. `arduino-cli` was not available in the project environment, so no compile/upload test was run. The source wiring applies only to the Freenove-style five-pin joystick shown. Direction labels depend on physical module orientation, and individual modules can have different center readings; the lesson therefore calibrates center at startup and treats it as an observation exercise, not a control for machinery, vehicles, or safety-critical systems.
