# Lesson 15 review — More Lights Than Pins

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/15-more-lights-than-pins.html`
- Local reference asset: `web/assets/lesson-15/lesson-15-freenove-74hc595-circuit.png`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_15.py`

## Reference validation

Primary retained source: `sources/freenove-ultimate-starter-kit/`, exact upstream revision `5315f61497eea49553aa1b70721751fb16a497e5`, under CC BY-NC-SA 3.0 as recorded in `SOURCES.md`. The public primary reference checked was [Freenove Chapter 15 — LED Matrix, Project 15.1 74HC595](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/15_LED_Matrix.html). The retained source sketch checked was `Sketches/Sketch_15.1.1_74HC595/Sketch_15.1.1_74HC595.ino`, lines 9–35. Pin functions and output-enable/reset roles were cross-checked against retained `Datasheet/74HC595.pdf`, extracted lines 86–101, and `shiftOut()` behavior against [Arduino documentation](https://docs.arduino.cc/language-reference/en/functions/advanced-io/shiftOut/).

| Lesson claim | Reference evidence | Result |
|---|---|---|
| Project 15.1 needs a control board, breadboard, USB cable, 74HC595, LED bar graph, eight 220 Ω resistors, and 17 M/M jumpers | Freenove Chapter 15 Project 15.1 component list; retained PDF printed page 125 / PDF page 129 | Pass |
| A 74HC595 converts one byte of serial data into eight parallel output choices | Freenove Chapter 15 component knowledge | Pass |
| Arduino D11 goes to DS/pin 14, D13 to SH_CP/pin 11, and D12 to ST_CP/pin 12 | Freenove Project 15.1 circuit, retained sketch lines 9–11, and local reference page | Pass |
| VCC/pin 16 and MR/pin 10 go to 5 V; GND/pin 8 and OE/pin 13 go to GND | Freenove Project 15.1 schematic; retained 74HC595 datasheet pin/enable descriptions | Pass |
| The LED bar graph has one distinct 220 Ω series resistor path per LED | Freenove Project 15.1 schematic and component list | Pass |
| The reference sketch shifts `0x01` with `LSBFIRST`, latches it, shifts left, and delays 100 ms, yielding a travelling light | Retained sketch lines 20–34 and public Chapter 15 sketch | Pass |
| `shiftOut()` transmits a byte serially using the given data/clock pins and bit order | Arduino `shiftOut()` reference | Pass |

The learner sketch is original: it introduces a small `showPattern()` helper and names the moving byte `pattern`, while retaining the source-validated D11/D13/D12 mapping, `LSBFIRST` transmission, low-then-high latch sequence, `0x01` starting value, one-bit left shift, and 100 ms interval. The page links actual public technical references in a section titled exactly **Reference pages**.

## Attribution and image handling

- `lesson-15-freenove-74hc595-circuit.png` is a non-generated, unchanged 1241 × 1754 PNG rasterization of the Freenove `Tutorial.pdf` Chapter 15 Project 15.1 circuit page (printed page 128 / PDF page 132).
- The image was visually inspected after export. It visibly contains the schematic and hardware connection, including the eight 220 Ω resistor paths, LED bar graph, 74HC595, and Arduino pin 11/12/13 paths.
- Its nearby caption visibly attributes Freenove; identifies Chapter 15, Project 15.1, printed/PDF pages; identifies the image as unchanged; links CC BY-NC-SA 3.0; and points to the bottom reference section.
- Freenove’s upstream repository declares all repository files CC BY-NC-SA 3.0. This project is original and noncommercial; attribution and share-alike conditions remain visible. `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_15.py -v` initially failed as expected because the Week 15 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_15.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **30 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/15-more-lights-than-pins.html`:
  - heading rendered as “More Lights Than Pins”; the local Freenove image loaded (`complete: true`, natural size `1241 × 1754`); and the “Reference pages” heading rendered;
  - five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, a particular 74HC595 or LED-bar-graph pinout, resistor values, USB power, any wiring, an Arduino upload, or the observed travelling-light effect. `arduino-cli` was not installed in the project environment, so no compile/upload test was run. The lesson is deliberately limited to the Freenove-style eight-segment bar graph and 74HC595 circuit shown in the reference: similar parts can have different physical pin maps or electrical characteristics. Learners are told to stop, unplug USB, and consult their exact part documentation rather than guess when their components differ.
