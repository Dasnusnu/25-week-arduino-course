# Lesson 11 review — Words on a Real Screen

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/11-words-on-a-real-screen.html`
- Local reference asset: `web/assets/lesson-11/lesson-11-freenove-i2c-lcd1602-circuit.png`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_11.py`

## Reference validation

Primary retained source: `sources/freenove-ultimate-starter-kit/`, exact upstream revision `5315f61497eea49553aa1b70721751fb16a497e5`, under CC BY-NC-SA 3.0 as recorded in `SOURCES.md`. Source sketch checked: `Sketches/Sketch_16B_I2C_LCD1602/Sketch_16.1.1_Display_the_string_on_LCD1602/Sketch_16.1.1_Display_the_string_on_LCD1602.ino`, lines 8–37. Public primary reference checked: [Freenove Chapter 16 — LCD1602](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/16_LCD1602.html).

| Lesson claim | Reference evidence | Result |
|---|---|---|
| LCD1602 is a 16-column, 2-line I2C display | Chapter 16, I2C LCD1602 component knowledge | Pass |
| I2C display uses VCC, GND, SDA, SCL and its circuit needs four connections | Chapter 16 component knowledge and Project 16.1 circuit image | Pass |
| Uno-compatible wiring uses 5V, GND, SDA/A4, SCL/A5 | Standard Uno-compatible I2C mapping; lesson scopes this to classic Uno-compatible boards and tells other-board users to use their documented I2C pins | Pass, scoped |
| Source sketch starts at 0x27 and falls back to 0x3F after an I2C transmission test | Retained sketch lines 11–16 and 30–37; public Chapter 16 sketch | Pass |
| `lcd.init()`, `lcd.backlight()`, `lcd.print()`, and `lcd.setCursor(0, 1)` produce the two-row text/counter behavior | Retained sketch lines 17–27 and Chapter 16 API explanation | Pass |
| Second row is row index 1 because cursor coordinates begin at zero | Chapter 16 sketch explanation | Pass |
| Contrast may need adjustment when backlight is present but characters are unclear | Chapter 16 post-upload guidance | Pass |

The displayed learner sketch is original: it retains the source-validated address check and LCD API behavior while using its own greeting, helper function name, safety language, and presentation. It links the real public reference pages in a section titled exactly **Reference pages**.

## Attribution and image handling

- `lesson-11-freenove-i2c-lcd1602-circuit.png` is an exact, non-generated download of Freenove’s public Chapter 16 Project 16.1 circuit-connection image (`Chapter16B_03.png`), verified as a valid 781 × 283 PNG.
- Its visible figure caption attributes Freenove, identifies Chapter 16 / Project 16.1, states the image is unchanged, links CC BY-NC-SA 3.0, and points to the bottom reference section.
- Freenove’s upstream repository declares all its files CC BY-NC-SA 3.0. This project is original and noncommercial; the attribution and share-alike condition remain visible. `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_11.py -v` initially failed as expected because the Week 11 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_11.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **22 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `http://127.0.0.1:8892/lessons/11-words-on-a-real-screen.html`:
  - heading rendered as “Words on a Real Screen”; the local Freenove image loaded (`complete: true`, natural width `781`); and the “Reference pages” heading rendered;
  - five checklist controls rendered at `0 of 5 checks complete.`;
  - a visible click on the first checkbox changed the UI to `1 of 5 checks complete.` with progress value `1`;
  - a visible click on `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]` under `25week-guide:/lessons/11-words-on-a-real-screen.html:checks`.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, a specific LCD1602/I2C backpack, its address, contrast potentiometer, library installation, wiring, upload, or actual visible LCD output. I2C LCD modules vary: the 0x27/0x3F fallback follows Freenove’s example but does not guarantee every module’s address. The A4/A5 instruction applies only to classic Uno-compatible boards; learners with another board must use that board’s documented I2C pins.
