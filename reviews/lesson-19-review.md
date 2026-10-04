# Lesson 19 review — A Clock That Never Forgets

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/19-a-clock-that-never-forgets.html`
- Local reference asset: `web/assets/lesson-19/lesson-19-erriez-ds1302-module.png`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_19.py`

## Reference validation

Primary retained source: `sources/erriez-ds1302-mit/`, supplied under the MIT License (Copyright 2020 Erriez), as recorded in `SOURCES.md`. The local `README.md` was checked at lines 5, 20–26, 53–85, 88–155, and 259–269; the exact retained source sketch checked was `examples/ErriezDS1302SetGetDateTime/ErriezDS1302SetGetDateTime.ino`, lines 32–55 and 66–144. The official DS1302 datasheet retained at `extras/DS1302.pdf`, printed pages 1–5, was checked for its clock/calendar purpose, CE/I/O/SCLK interface roles, power pins, and battery/trickle-charge constraints. The public primary references are linked in the lesson's section titled exactly **Reference pages**.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| DS1302 is a real-time clock/calendar using a three-wire CE/I/O/SCLK interface | Erriez README lines 5 and 259–269; DS1302 datasheet pages 1–2 and 4–5 | Pass |
| Its three-wire interface is not SPI | Erriez README line 26 | Pass |
| AVR/Uno mapping is CLK D2, I/O D3, CE D4, with GND and VCC2 connected to board power | Erriez README lines 58–76 and 263–269; Set/Get example lines 35–55 | Pass |
| Learner-facing breakout labels map CLK/SCLK, DAT/I/O, and RST/CE without presuming header order | Datasheet page 4 names SCLK, I/O, CE and notes earlier datasheets called CE “RST”; retained Erriez source supplies the matching logical pins | Pass |
| The code constructs `ErriezDS1302` from the three pins, initializes it, sets date/time, reads date/time, and updates once each second | Set/Get example lines 54–55, 80–89, 103–143; README lines 123–154 | Pass |
| The one-time-setting switch prevents a learner’s stored value being overwritten on every reset after initial setup | Source `setDateTime()` behavior plus original presentation; the retained example always writes its fixed demonstration time in `setup()` | Pass |
| Date/time value order and ranges are accurately described | Erriez README lines 125–154 | Pass |
| DS1302 time can deviate more than one minute per day and is not for new precision designs | Erriez README lines 22–25 | Pass |
| Backup/trickle-charge guidance does not assume a battery type or enable charging | DS1302 datasheet pages 2 and 4; Erriez README lines 228–240 | Pass |

The lesson confines itself to a labeled low-voltage DS1302 breakout. It instructs learners not to substitute bare-chip pin names for a module header, not to guess backup battery type or rechargeability, and not to use the optional trickle charger. It explicitly covers coin-cell swallowing risk and prohibits shorting, heating, crushing, disassembling, or charging the cell. It also distinguishes a learning clock from precise or safety-critical timing.

## Attribution and image handling

- `lesson-19-erriez-ds1302-module.png` is an unchanged 200 × 171 PNG copy of `sources/erriez-ds1302-mit/extras/DS1302.png`.
- The image was visually inspected. It is a non-generated photo of a green DS1302 module with the DS1302 IC, crystal, coin-cell holder, and a five-pin header; its header labels are not legible enough to use as a wiring map, which the lesson explicitly says.
- Its nearby caption visibly identifies Erriez, original source path, unchanged status, and MIT License, with a link to the exact public license and the bottom reference section.
- The Erriez retained source is MIT-licensed. This project preserves attribution in the lesson caption and reference section; `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_19.py -v` initially failed as expected because the Week 19 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_19.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **38 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/19-a-clock-that-never-forgets.html`:
  - heading rendered as “A Clock That Never Forgets”; the local Erriez image loaded (`complete: true`, natural size `200 × 171`); the “Reference pages” heading rendered; and five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, any particular DS1302 breakout, its printed pin labels, a coin-cell holder, battery chemistry/condition, actual backup retention, oscillator accuracy, serial output, Arduino compilation/upload, or observed timekeeping. `arduino-cli` is not installed in the project environment, so no compile/upload test was run. DS1302 breakout layouts and battery arrangements vary; learners must use exact module documentation and never infer battery safety or pin order from the reference photo.