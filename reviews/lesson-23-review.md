# Lesson 23 review — Green Light, Red Light

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/23-green-light-red-light.html`
- Local reference asset: `web/assets/lesson-23/lesson-23-freenove-led-circuit.jpg`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_23.py`

## Reference validation

Primary retained source: `sources/freenove-ultimate-starter-kit/`, exact upstream revision `5315f61497eea49553aa1b70721751fb16a497e5`, under CC BY-NC-SA 3.0 as recorded in `SOURCES.md`. The public primary reference checked was [Freenove Chapter 1 — LED Blink](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/1_LED_Blink.html). Its retained `Tutorial.pdf` circuit page (printed page 20) and the project’s existing source-licensed rasterization were inspected for its one-LED branch: a digital output pin, 220 Ω resistor, LED, and ground. The exact public source context for the curriculum title was also checked in the retained MIT repository `sources/rfid-door-lock-mit/`: `main.cpp` lines 31–63 has its separate RFID/UID comparison and LCD/servo access-control behavior. That behavior is explicitly excluded rather than adapted. The actual public pages are linked in the lesson section titled exactly **Reference pages**.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| A low-voltage LED branch can run from an Arduino digital output through a 220 Ω resistor and LED to ground | Freenove Chapter 1 and retained Tutorial.pdf printed page 20 | Pass |
| Two indicators need two separate current-limiting branches | The validated one-LED topology is repeated as two original, independent branches; each retains a 220 Ω resistor | Pass |
| The status sketch sets output pins with `pinMode()` and drives one LED while turning the other off with `digitalWrite()` | Original code inspection; it uses D5/D6 only, no libraries or actuator APIs | Pass |
| The upstream RFID source has true/false access-related branches, but also drives a servo and reports access through an LCD | Retained `main.cpp` lines 38–58 | Pass — all RFID, UID comparison, LCD, servo, delay, and door behavior deliberately excluded |

The lesson’s D5/D6 pin assignment and Serial Monitor `g`/`r` interaction are original teaching choices, not copied source code. The page states that it is a manual lab/demo status indicator, not an access-control system. It does not read RFID, store or compare UIDs, use an allow list, move a servo, control a relay, or make an entry decision. It instructs learners to use a 220 Ω resistor for each LED, disconnect USB before rewiring, inspect damaged/hot parts safely, and never connect this circuit to locks, relays, or real access systems.

## Attribution and image handling

- `lesson-23-freenove-led-circuit.jpg` is a non-generated, unchanged 910 × 1287 JPEG duplicate of the project’s source-licensed Chapter 1 Freenove rasterization. SHA-256: `53268834716137ef5191137ae83f8c0389c901b8edee1ef47846e6aef27b6744`.
- The image is an unchanged rasterization of Freenove Ultimate Starter Kit `Tutorial.pdf`, Chapter 1 LED Blink, printed page 20. It visibly shows the reference one-LED topology: pin 13, R1 220 Ω, LED1, and ground, plus the corresponding breadboard view.
- Its nearby caption visibly identifies Freenove, source chapter/page, unchanged status, CC BY-NC-SA 3.0, the limited one-branch purpose, and links to the exact public tutorial, license, and bottom reference section.
- Freenove’s upstream repository declares CC BY-NC-SA 3.0, and the lesson retains visible attribution, noncommercial, and ShareAlike notice. `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_23.py -v` initially failed as expected because the Week 23 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_23.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **46 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/23-green-light-red-light.html`:
  - heading rendered as “Green Light, Red Light”; the attributed local image loaded (`complete: true`, natural size `910 × 1287`); the “Reference pages” heading rendered; and five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`;
  - the browser’s full-page screenshot capture timed out after the interaction checks completed; this did not affect the returned DOM, image-load, or checklist/reset assertions.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, either LED color/direction/forward voltage, the 220 Ω resistors, breadboard wiring, D5/D6 outputs, USB supply, Arduino compilation/upload, Serial Monitor transmission, or observed LED behavior. `arduino-cli` is not installed in the project environment, so no compile/upload test was run. LED characteristics and board pinouts vary; learners must confirm their exact board and components. This deliberately non-authorizing visual exercise must not be converted into a lock, real access-control, RFID authorization, or other safety/security decision system.
