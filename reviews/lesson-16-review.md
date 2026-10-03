# Lesson 16 review — Small Board, Big Switch

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/16-small-board-big-switch.html`
- Local reference asset: `web/assets/lesson-16/lesson-16-freenove-relay-circuit.png`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_16.py`

## Reference validation

Primary retained source: `sources/freenove-ultimate-starter-kit/`, exact upstream revision `5315f61497eea49553aa1b70721751fb16a497e5`, under CC BY-NC-SA 3.0 as recorded in `SOURCES.md`. The public primary reference checked was [Freenove Chapter 10 — Motor, Project 10.1 Control Motor by Relay](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/10_Motor.html). The retained source sketch checked was `Sketches/Sketch_10.1.1_Control_Motor_by_Relay/Sketch_10.1.1_Control_Motor_by_Relay.ino`, lines 9–45. The local tutorial’s extracted text at `Tutorial.pdf` lines 1248–1333 was also checked against the image and sketch. `digitalRead()` and `digitalWrite()` behavior were cross-checked against the linked Arduino reference pages.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| Project 10.1 uses a control board, breadboard, USB cable, eight M/M jumpers, two-AA holder, two 10 kΩ resistors, 1 kΩ resistor, 220 Ω resistor, NPN transistor, 5 V relay, small motor, push button, LED, and diode | Freenove Chapter 10 Project 10.1 component list; retained PDF printed pages 90–91 / extracted lines 1248–1258 | Pass |
| Arduino D12 detects the push button and D9 controls the relay circuit | Freenove Project 10.1 circuit and retained sketch lines 9–10, 18–20 | Pass |
| The reference circuit uses an NPN-transistor relay driver, a diode across the coil, and an LED with 220 Ω resistor | Freenove schematic on retained PDF printed page 93 / PDF page 97; public Chapter 10 circuit | Pass |
| The motor is powered by a separate two-AA-battery supply | Freenove Project 10.1 circuit description and schematic; retained PDF lines 1281–1282 | Pass |
| The normal button state is HIGH and a stable LOW press toggles `relayState` after more than 10 ms | Retained sketch lines 12–14 and 25–44; public Chapter 10 sketch | Pass |
| The original learner sketch retains D12/D9, initial relay-off state, stable-time debounce, and one-toggle-per-press behavior | Source-validated elements above; naming and control-flow presentation are original | Pass |
| `digitalRead()` returns HIGH or LOW and `digitalWrite()` sets an OUTPUT HIGH or LOW | Linked Arduino digitalRead/digitalWrite references | Pass |

The lesson deliberately identifies the source circuit as a bare relay/transistor circuit, not a generic three-pin relay module. It is explicitly scoped to the source’s USB 5 V control and separate two-AA low-voltage motor circuit. It never gives AC-mains or line-voltage instructions, explicitly prohibits such connections, and preserves the source warning boundaries around moving parts and powered rewiring. The page links actual public technical references in a section titled exactly **Reference pages**.

## Attribution and image handling

- `lesson-16-freenove-relay-circuit.png` is a non-generated, unchanged 1241 × 1754 PNG rasterization of the Freenove `Tutorial.pdf` Chapter 10 Project 10.1 circuit page (printed page 93 / PDF page 97).
- The image was visually inspected after export. It visibly contains the Project 10.1 schematic, including the D12 button input, D9 transistor driver, relay, diode, LED/resistor indicator path, two-cell battery holder, and motor.
- Its nearby caption visibly attributes Freenove; identifies Chapter 10, Project 10.1, printed/PDF pages; identifies the image as unchanged; links CC BY-NC-SA 3.0; and points to the bottom reference section.
- Freenove’s upstream repository declares all repository files CC BY-NC-SA 3.0. This project is original and noncommercial; attribution and ShareAlike conditions remain visible. `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_16.py -v` initially failed as expected because the Week 16 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_16.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **32 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/16-small-board-big-switch.html`:
  - heading rendered as “Small Board, Big Switch”; the local Freenove image loaded (`complete: true`, natural size `1241 × 1754`); and the “Reference pages” heading rendered;
  - five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, a specific relay, transistor, diode, motor, battery holder, the exact component pinouts, USB power, battery polarity, wiring, Arduino upload, or observed relay/motor behavior. `arduino-cli` was not installed in the project environment, so no compile/upload test was run. The full-page screenshot capture timed out after the browser interaction data had already returned, so the recorded browser evidence is DOM/runtime data rather than a saved screenshot. Learners must stop and consult documentation for any relay, diode, motor, or module that differs from the pictured Freenove kit parts. This lesson intentionally excludes AC mains, line voltage, house wiring, and other high-voltage loads.
