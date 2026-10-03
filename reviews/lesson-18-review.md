# Lesson 18 review — Point It Anywhere

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/18-point-it-anywhere.html`
- Local reference asset: `web/assets/lesson-18/lesson-18-freenove-servo-pot-circuit.png`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_18.py`

## Reference validation

Primary retained source: `sources/freenove-ultimate-starter-kit/`, exact upstream revision `5315f61497eea49553aa1b70721751fb16a497e5`, under CC BY-NC-SA 3.0 as recorded in `SOURCES.md`. The public primary reference checked was [Freenove Chapter 11 — Servo, Project 11.2](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/11_Servo.html). The retained source sketch checked was `Sketches/Sketch_11.2.1_Control_Servo_by_Potentiometer/Sketch_11.2.1_Control_Servo_by_Potentiometer.ino`, lines 9–25. The local tutorial text at `Tutorial.pdf` lines 3847–3869, 3880–3884, and 3953–4022 was checked against the circuit image and sketch. Arduino’s Servo library, Servo Motor Basics/Knob, and `analogRead()` pages were checked for library behavior, power/load limits, and Uno’s 10-bit input range.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| Project 11.2 uses a control board, breadboard, USB cable, six M/M jumpers, a rotary potentiometer, and a servo | Freenove Chapter 11 Project 11.2 component list; retained PDF printed page 107 / extracted lines 3953–3973 | Pass |
| The potentiometer is read at A0 and the matching servo signal is driven from pin 3 | Freenove Project 11.2 circuit; retained PDF printed page 108 / extracted line 3986 | Pass |
| The pictured matching servo lead assignment is orange signal, red VCC, brown GND | Freenove Chapter 11 component knowledge and servo circuit; retained PDF lines 3851–3853 and 3880–3884 | Pass |
| The source sketch reads A0, maps 0–1023 to 0–180, writes that angle, and pauses 15 ms | Retained sketch lines 13–25; public Chapter 11 Project 11.2 sketch; retained PDF lines 4003–4022 | Pass |
| The original learner sketch retains the source A0/pin-3 mapping, 0–1023 to 0–180 mapping, Servo library use, angle write, and 15 ms timing | Source-validated elements above; clearer names and safety framing are original presentation | Pass |
| An Uno’s default `analogRead()` is a 10-bit 0–1023 value | Linked Arduino `analogRead()` page | Pass |
| Servo current demand rises with motion/load; heavier, larger, or multiple-servo designs need a rated external low-voltage supply with common ground | Linked Arduino Servo library and Servo Motor Basics/Knob pages | Pass |

The lesson is limited to the source’s matching small, unloaded kit servo and its pictured low-voltage circuit. It explicitly prohibits powered rewiring, forced or blocked movement, loads, mains/wall power, unknown supplies, and inferring another servo’s lead order. For any larger, loaded, different, or multi-servo design it tells learners to stop and consult the exact servo specifications and external-power documentation. The page links actual public technical references in a section titled exactly **Reference pages**.

## Attribution and image handling

- `lesson-18-freenove-servo-pot-circuit.png` is a non-generated, unchanged 1241 × 1754 PNG rasterization of the Freenove `Tutorial.pdf` Chapter 11 Project 11.2 circuit page (printed page 108 / PDF page 112).
- The image was visually inspected after export. It visibly shows the Project 11.2 circuit: potentiometer outer terminals to 5 V/GND with its centre connection to A0, and the servo signal/VCC/GND paths to pin 3/5 V/GND.
- Its nearby caption visibly attributes Freenove; identifies Chapter 11, Project 11.2, printed/PDF pages; identifies the image as unchanged; links CC BY-NC-SA 3.0; and points to the bottom reference section.
- Freenove’s upstream repository declares all repository files CC BY-NC-SA 3.0. This project is original and noncommercial; attribution and ShareAlike conditions remain visible. `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_18.py -v` initially failed as expected because the Week 18 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_18.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **36 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/18-point-it-anywhere.html`:
  - heading rendered as “Point It Anywhere”; the local Freenove image loaded (`complete: true`, natural size `1241 × 1754`); the “Reference pages” heading rendered; and five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, the kit servo, potentiometer, breadboard, USB supply, individual wire colours, actual current draw, mechanical end stops, heat, noise, horn travel, Arduino compilation/upload, or observed motion. `arduino-cli` is not installed in the project environment, so no compile/upload test was run. Servo variants differ in lead order, travel, voltage, and current requirements; learners must consult the exact component documentation before using another servo or any external supply.
