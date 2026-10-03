# Lesson 12 review — The Secret Password Pad

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/12-the-secret-password-pad.html`
- Local reference asset: `web/assets/lesson-12/lesson-12-freenove-combination-lock-circuit.png`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_12.py`

## Reference validation

Primary retained source: `sources/freenove-ultimate-starter-kit/`, exact upstream revision `5315f61497eea49553aa1b70721751fb16a497e5`, under CC BY-NC-SA 3.0 as recorded in `SOURCES.md`. Source sketches checked: `Sketches/Sketch_19.1.1_Get_Input_Characters/Sketch_19.1.1_Get_Input_Characters.ino`, lines 9–36, and `Sketches/Sketch_19.2.1_Combination_Lock/Sketch_19.2.1_Combination_Lock.ino`, lines 9–67. Public primary reference checked: [Freenove Chapter 19 — Matrix Keypad](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/19_Matrix_Keypad.html). Servo safety/power guidance was checked against [Arduino Servo library documentation](https://docs.arduino.cc/libraries/servo/).

| Lesson claim | Reference evidence | Result |
|---|---|---|
| A 4×4 keypad returns 16 character positions by scanning four rows and four columns | Freenove Chapter 19 component knowledge and Project 19.1 | Pass |
| Key labels are `1 2 3 A`, `4 5 6 B`, `7 8 9 C`, `* 0 # D` | Retained Project 19.1 sketch lines 12–17 | Pass |
| Keypad connector pins 8–1 route respectively to D11–D4 | Freenove Project 19.2 circuit image and retained sketches lines 20–24 | Pass |
| Combination-lock design uses D13 through a 1 kΩ resistor and NPN transistor for the active buzzer | Freenove Project 19.2 circuit image and retained sketch lines 27–28, 35, 43–47, 62–65 | Pass |
| Servo signal is D12 and the source behavior starts at 45°, moves to 135° for 2 seconds on a correct four-character entry, then returns | Freenove Project 19.2 circuit image and retained sketch lines 26–34, 51–60 | Pass |
| Four key presses are buffered, compared, then cleared for a new attempt | Retained Project 19.2 sketch lines 39–40, 49–67 | Pass |
| Servo power/ground and moving-load cautions are necessary | Arduino Servo documentation; lesson restricts the source design to one small, unloaded kit servo and USB power | Pass, scoped |

The learner sketch is original: it presents a different secret (`2580`), names and organizes its own helpers, and explains the state flow in original language while retaining source-validated pin assignments and actuator behavior. It links actual public technical pages in a section titled exactly **Reference pages**.

## Attribution and image handling

- `lesson-12-freenove-combination-lock-circuit.png` is a non-generated crop of Freenove’s Chapter 19 Project 19.2 circuit page from the retained `Tutorial.pdf` (PDF page 182 / printed page 178). It retains the complete circuit headings, keypad, buzzer/transistor, servo wiring, and hardware layout; only surrounding page matter was removed.
- The image was inspected after export and is a valid 1040 × 920 PNG.
- Its visible figure caption attributes Freenove, identifies Chapter 19 / Project 19.2 and the source PDF page, identifies the crop as otherwise unchanged, links CC BY-NC-SA 3.0, and points to the bottom reference section.
- Freenove’s upstream repository declares all its files CC BY-NC-SA 3.0. This project is original and noncommercial; attribution and share-alike conditions remain visible. `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_12.py -v` initially failed as expected because the Week 12 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_12.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **24 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `http://127.0.0.1:8893/lessons/12-the-secret-password-pad.html`:
  - heading rendered as “The Secret Password Pad”; the local Freenove image loaded (`complete: true`, natural width `1040`); and the “Reference pages” heading rendered;
  - five checklist controls rendered at `0 of 5 checks complete.`;
  - a visible click on the first checkbox changed the UI to `1 of 5 checks complete.` with progress value `1` and stored `["1"]`;
  - a visible click on `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]` under `25week-guide:/lessons/12-the-secret-password-pad.html:checks`.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, keypad connector orientation, a specific NPN transistor’s pinout, active buzzer, servo, USB power capability, library installation, wiring, upload, sound, or servo movement. `arduino-cli` was not available in the project environment, so no compile/upload test was run. The keypad pin sequence applies only to the Freenove-style keypad and source layout shown. Servo angles and available current can differ by hardware; the lesson intentionally treats the build as an unloaded desk demonstration, not a real lock or a safety/security device.
