# Lesson 17 review — The Precision Spinner

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/17-the-precision-spinner.html`
- Local reference asset: `web/assets/lesson-17/lesson-17-freenove-stepper-circuit.png`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_17.py`

## Reference validation

Primary retained source: `sources/freenove-ultimate-starter-kit/`, exact upstream revision `5315f61497eea49553aa1b70721751fb16a497e5`, under CC BY-NC-SA 3.0 as recorded in `SOURCES.md`. The public primary reference checked was [Freenove Chapter 18 — Stepper Motor, Project 18.1](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/18_Stepper_Motor.html). The retained source sketch checked was `Sketches/Sketch_18.1.1_Drive_Stepper_Motor/Sketch_18.1.1_Drive_Stepper_Motor.ino`, lines 9–49. The local tutorial’s extracted text at `Tutorial.pdf` lines 6359–6467 and 6469–6507 was checked against the image and sketch. `digitalWrite()` and `delay()` behavior were cross-checked against the linked Arduino reference pages.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| Project 18.1 uses a control board, USB cable, matching stepper motor, ULN2003 driver, and six F/M jumpers | Freenove Chapter 18 Project 18.1 component list; retained PDF printed page 166 / extracted lines 6359–6367 | Pass |
| Arduino D11/D10/D9/D8 connect to ULN2003 IN1/IN2/IN3/IN4, with 5 V to VCC and GND to GND | Freenove Project 18.1 circuit and retained PDF printed page 169 / extracted lines 6443–6456 | Pass |
| The supplied geared output shaft needs 32 × 64 = 2,048 full steps per revolution | Freenove Chapter 18 component knowledge; retained PDF lines 6423–6426 | Pass |
| The ULN2003 receives weak control inputs and drives the supplied four-phase motor; its PWR and VCC are connected by default | Freenove Chapter 18 ULN2003 description; retained PDF lines 6427–6431 | Pass |
| The source sketch configures D11/D10/D9/D8 as outputs, makes 2,048 steps at 2 ms each, pauses 1,000 ms, and repeats in the opposite direction | Retained sketch lines 9–48; public Chapter 18 sketch | Pass |
| The original learner sketch retains the source pin order, full-turn count, one-coil sequence, 2 ms timing, and forward/reverse behavior | Source-validated elements above; clearer names and conditional expression are original presentation | Pass |
| `digitalWrite()` writes HIGH/LOW to an output and `delay(ms)` pauses for the requested millisecond duration | Linked Arduino digitalWrite/delay reference pages | Pass |

The lesson specifies only the source’s matching low-voltage kit board, ULN2003 driver, and geared stepper. It explicitly prohibits direct motor-to-pin connections, unknown power, wall outlets, mains, forced shaft movement, and powered rewiring. The page links actual public technical references in a section titled exactly **Reference pages**.

## Attribution and image handling

- `lesson-17-freenove-stepper-circuit.png` is a non-generated, unchanged 1241 × 1754 PNG rasterization of the Freenove `Tutorial.pdf` Chapter 18 Project 18.1 circuit page (printed page 169 / PDF page 173).
- The image was visually inspected after export. It visibly shows the D11/D10/D9/D8 to IN1/IN2/IN3/IN4 diagram, 5 V/VCC and GND/GND, ULN2003 board, and matching motor connection.
- Its nearby caption visibly attributes Freenove; identifies Chapter 18, Project 18.1, printed/PDF pages; identifies the image as unchanged; links CC BY-NC-SA 3.0; and points to the bottom reference section.
- Freenove’s upstream repository declares all repository files CC BY-NC-SA 3.0. This project is original and noncommercial; attribution and ShareAlike conditions remain visible. `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_17.py -v` initially failed as expected because the Week 17 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_17.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **34 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/17-the-precision-spinner.html`:
  - heading rendered as “The Precision Spinner”; the local Freenove image loaded (`complete: true`, natural size `1241 × 1754`); and the “Reference pages” heading rendered;
  - five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, ULN2003 board, motor, connector, individual driver board jumper, USB supply, actual wiring, Arduino upload, motor direction, torque, heat, noise, or observed movement. `arduino-cli` is not installed in the project environment, so no compile/upload test was run. Learners must stop and consult documentation for any driver or motor that differs from the pictured Freenove kit parts. This lesson intentionally excludes mains, line voltage, and unknown/external power supplies.
