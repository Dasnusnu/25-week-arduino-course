# Lesson 20 review — Control It by Remote

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/20-control-it-by-remote.html`
- Local reference asset: `web/assets/lesson-20/lesson-20-freenove-ir-receiver-circuit.png`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_20.py`

## Reference validation

Primary retained source: `sources/freenove-ultimate-starter-kit/`, exact upstream revision `5315f61497eea49553aa1b70721751fb16a497e5`, under CC BY-NC-SA 3.0 as recorded in `SOURCES.md`. The public primary reference checked was [Freenove Chapter 21 — Infrared Remote, Project 21.1](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/21_Infrared_Remote.html). The retained source sketch checked was `Sketches/Sketch_21.1.1_Infrared_Remote_Control/Sketch_21.1.1_Infrared_Remote_Control.ino`, lines 9–28. The local tutorial text at `Tutorial.pdf` printed pages 187–190 / PDF pages 191–194 was checked, including the Project 21.1 circuit at printed page 189 / PDF page 193. The current [Arduino-IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote) README and [SimpleReceiver example](https://github.com/Arduino-IRremote/Arduino-IRremote/blob/master/examples/SimpleReceiver/SimpleReceiver.ino) were checked for its current `IRremote.hpp` / `IrReceiver` API. The actual public pages are linked in the lesson section titled exactly **Reference pages**.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| Project 21.1 uses a control board, breadboard, USB cable, IR remote, IR receiver, four jumpers, and a 10 kΩ resistor | Freenove Chapter 21 Project 21.1 component list; retained PDF printed page 187 / PDF page 191 | Pass |
| The remote encodes button presses in IR light and receiver DATA outputs the received IR signal | Freenove Chapter 21 component knowledge | Pass |
| The Freenove Project 21.1 circuit uses receiver DATA to pin 12, VCC to 5 V, GND to GND, and a 10 kΩ pull-up from DATA to 5 V | Freenove Chapter 21 circuit; retained PDF printed page 189 / PDF page 193 | Pass |
| The retained legacy sketch uses D12, 9600 baud, starts reception, decodes a result, prints hexadecimal data, resumes, and waits 100 ms | Retained Sketch 21.1.1 lines 9–28; public Chapter 21 sketch | Pass |
| The original learner sketch keeps D12 and 9600 baud but uses the maintained current library API | Current Arduino-IRremote README “Receiving IR codes” and `SimpleReceiver.ino` lines 72–119 | Pass |
| Current API flow is `IrReceiver.begin()`, `IrReceiver.decode()`, read `decodedIRData`, then `IrReceiver.resume()` | Current Arduino-IRremote README “Receiving IR codes” / `decodedIRData`; `SimpleReceiver.ino` lines 86–119 | Pass |
| Holding a button can create repeat data; values cannot be assumed across different remotes/protocols | Arduino-IRremote README flags / protocol documentation | Pass |

The lesson is limited to the source’s labeled, low-voltage receiver circuit and a reading-only serial exercise. It instructs learners to unplug before rewiring, follow labels and exact module documentation, never infer a three-pin receiver’s pin order, and avoid mains/wall power. It covers coin-cell swallowing and misuse risks, documents that bright sunlight or lamps can introduce noise, and forbids using this lesson to control safety equipment, doors, appliances, or mains-powered devices.

## Attribution and image handling

- `lesson-20-freenove-ir-receiver-circuit.png` is a non-generated, unchanged 1241 × 1754 PNG rasterization of the Freenove `Tutorial.pdf` Chapter 21 Project 21.1 circuit page (printed page 189 / PDF page 193); SHA-256: `a65d34598e3f78e143c51e75ba9ff888c19f8cc1a9704e017bdb61e52b23ea88`.
- The rendered page was visually inspected. It visibly shows the receiver circuit: VCC to 5 V, GND to ground, DATA to pin 12, and R1 10 kΩ between DATA and 5 V, alongside the source hardware connection.
- Its nearby caption visibly identifies Freenove, Chapter 21 / Project 21.1, printed and PDF pages, unchanged status, and CC BY-NC-SA 3.0, with links to the exact public tutorial, license, and bottom reference section.
- Freenove’s upstream repository declares all repository files CC BY-NC-SA 3.0. This project is original and noncommercial; attribution and ShareAlike conditions remain visible. `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_20.py -v` initially failed as expected because the Week 20 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_20.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **40 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/20-control-it-by-remote.html`:
  - heading rendered as “Control It by Remote”; the local Freenove image loaded (`complete: true`, natural size `1241 × 1754`); the “Reference pages” heading rendered; and five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, the exact Freenove IR receiver or remote, receiver pin labels/order, the 10 kΩ resistor, breadboard wiring, remote battery condition, IR range/noise, decoded protocol/value, Arduino compilation/upload, or observed serial output. `arduino-cli` is not installed in the project environment, so no compile/upload test was run. IR receivers, breakout modules, remote protocols, and remote codes vary; learners must use their exact component documentation and record values observed from their own remote.
