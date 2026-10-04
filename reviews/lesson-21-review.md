# Lesson 21 review — The Remote-Controlled Lamp

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/21-the-remote-controlled-lamp.html`
- Local reference asset: `web/assets/lesson-21/lesson-21-freenove-remote-led-circuit.png`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_21.py`

## Reference validation

Primary retained source: `sources/freenove-ultimate-starter-kit/`, exact upstream revision `5315f61497eea49553aa1b70721751fb16a497e5`, under CC BY-NC-SA 3.0 as recorded in `SOURCES.md`. The public primary reference checked was [Freenove Chapter 21 — Infrared Remote](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/21_Infrared_Remote.html), especially Project 21.2. The retained source sketch checked was `Sketches/Sketch_21.2.1_Control_LED_through_Infrared_Remote/Sketch_21.2.1_Control_LED_through_Infrared_Remote.ino`, lines 9–55. The local tutorial circuit page checked was `Tutorial.pdf` printed page 192 / PDF page 196. The current [Arduino-IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote) README and [SimpleReceiver example](https://github.com/Arduino-IRremote/Arduino-IRremote/blob/master/examples/SimpleReceiver/SimpleReceiver.ino) were checked for current `IRremote.hpp`, `IrReceiver`, command, flags, and resume behavior. The actual public pages are linked in the lesson section titled exactly **Reference pages**.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| Project 21.2 uses an IR receiver, remote, LED, 10 kΩ resistor, and 220 Ω resistor, among other parts | Freenove Chapter 21 Project 21.2 component list; retained tutorial PDF printed page 191 / PDF page 195 | Pass |
| The source circuit uses receiver DATA to D12, VCC to 5 V, GND to GND, and a 10 kΩ DATA-to-5 V pull-up | Freenove Project 21.2 circuit, printed page 192 / PDF page 196; retained Project 21.2 sketch lines 11–13 | Pass |
| The source LED branch runs from D5 through LED1 and R3 (220 Ω) to ground | Freenove Project 21.2 circuit, printed page 192 / PDF page 196; retained Project 21.2 sketch lines 15 and 42–52 | Pass |
| The source’s D13 buzzer/transistor branch is separate from its D5 LED branch | Freenove Project 21.2 circuit, printed page 192 / PDF page 196; retained Project 21.2 sketch lines 16 and 35–39 | Pass |
| The retained legacy example decodes, handles a command, and resumes the IR receiver | Retained Project 21.2 sketch lines 27–32 | Pass |
| The original learner sketch keeps source D12/D5 assignments but uses current maintained IRremote API | Arduino-IRremote README and SimpleReceiver example: `IRremote.hpp`, `IrReceiver.begin()`, `decode()`, `decodedIRData.command`, repeat flag, and `resume()` | Pass |
| Command values must be measured from the learner’s remote rather than copied from the historical Freenove remote | Freenove historical sketch shows its model-specific raw values; Arduino-IRremote documents protocol/result data and repeat flags | Pass |

The lesson explicitly models only a low-voltage LED. It instructs learners to unplug USB before rewiring, follow receiver labels and exact module documentation, use a 220 Ω LED current-limiting resistor, and never infer a three-pin receiver’s pin order. It explicitly forbids AC mains/wall-outlet/household-lamp wiring and does not teach use of a relay or other mains control. It also covers coin-cell hazards, hot/damaged parts, and uses a code guard that leaves the LED off until the learner has entered their own observed commands.

## Attribution and image handling

- `lesson-21-freenove-remote-led-circuit.png` is a non-generated, unchanged 1241 × 1754 PNG rasterization of Freenove `Tutorial.pdf` Chapter 21 Project 21.2 circuit page (printed page 192 / PDF page 196); SHA-256: `96971848f964fa2372f40a425ea2bed51181c51fa41e807972b2d9da403aed5f`.
- The rendered page was visually inspected. It visibly shows D12 to the receiver DATA node with R1 10 kΩ to 5 V, and D5 to LED1 with R3 220 Ω to ground. It also visibly separates the excluded D13 buzzer/transistor branch.
- Its nearby caption visibly identifies Freenove, Chapter 21 / Project 21.2, printed and PDF pages, unchanged status, and CC BY-NC-SA 3.0, with links to the exact public tutorial, license, and bottom reference section.
- Freenove’s upstream repository declares all repository files CC BY-NC-SA 3.0. This project is original and noncommercial; attribution and ShareAlike conditions remain visible. `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_21.py -v` initially failed as expected because the Week 21 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_21.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **42 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/21-the-remote-controlled-lamp.html`:
  - heading rendered as “The Remote-Controlled Lamp”; the local Freenove image loaded (`complete: true`, natural size `1241 × 1754`); the “Reference pages” heading rendered; and five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`;
  - heading hierarchy and visible image were checked in the rendered document.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, the exact Freenove IR receiver/remote/LED, receiver pin order, the 10 kΩ or 220 Ω resistor, breadboard wiring, remote battery condition, IR range/noise, decoded protocol/command values, Arduino compilation/upload, or observed LED behavior. `arduino-cli` is not installed in the project environment, so no compile/upload test was run. IR receivers, breakout modules, remote protocols, command values, and LED characteristics vary; learners must use their exact component documentation and values observed from their own remote.
