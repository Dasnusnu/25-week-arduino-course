# Lesson 25 review — The RFID Door Lock

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/25-the-rfid-door-lock.html`
- Reused local reference asset: `web/assets/lesson-22/lesson-22-mit-rfid-wiring-table.png`
- Lesson-directory route: `web/app.js`
- Curriculum metadata: `data/lessons.json`
- Focused static contract: `tests/test_lesson_25.py`

## Reference validation

Primary retained source: `sources/rfid-door-lock-mit/` at upstream commit `b82c0a13299f87d8540689303394beac567aa183` (`https://github.com/mithra1x/RFID-based-Smart-Door-Lock-System.git`). The local source was not modified. Its `LICENSE` is MIT (copyright 2025 Mikayıl Namazov); the public README, `main.cpp`, and license are linked from the lesson section titled exactly **Reference pages**.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| RC522/Uno wiring is SDA D10, SCK D13, MOSI D11, MISO D12, RST D9, GND GND, and 3.3V 3.3V | Retained README lines 30–40; public README wiring table | Pass |
| I2C LCD/Uno wiring is VCC 5V, GND GND, SDA A4, SCL A5 | Retained README lines 42–47; public README wiring table | Pass |
| The source’s matching small-servo connection is signal D3, VCC 5V, GND GND | Retained README lines 49–53; public README wiring table | Pass |
| The source initializes SPI, `MFRC522(10, 9)`, LCD `0x27` at 16×2, LCD init/backlight, servo pin 3, new-card/read-serial flow, and a halt call | Retained `main.cpp` lines 1–33 and 63 | Pass |
| The source then compares a four-byte UID, uses permission text, and moves a servo for a real-door purpose | Retained `main.cpp` lines 38–62; retained README lines 76–90 | Pass — deliberately excluded |

The original lesson sketch observes only a nearby user-owned/lab tag, displays `Tag seen` / `Bench demo only`, and moves only a light paper pointer between status marks. It contains no stored UID, UID comparison, allow list, card-memory operation, UID display, credential alteration, person/permission result, relay pin, or real-world mechanism command. Learner text explicitly says not to use it to secure people or property or operate a real door, gate, latch, relay, or mechanism.

## Attribution and image handling

- `lesson-22-mit-rfid-wiring-table.png` is a retained, non-generated, unchanged 1000 × 700 PNG capture of the public `mithra1x/RFID-based-Smart-Door-Lock-System` repository page.
- Its nearby visible caption names mithra1x, the repository, MIT License, unchanged status, and the **Reference pages** section. It is source context only; the connection paths are accessible text that was checked against the retained README tables.
- `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_25.py -v` initially failed as expected because the Week 25 page did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_25.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **50 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/25-the-rfid-door-lock.html`:
  - heading rendered as “The RFID Door Lock”; **Reference pages** rendered; the attributed local image loaded (`complete: true`, natural size `1000 × 700`); and five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`.
- The dashboard route is covered by the focused static contract, which checks `web/app.js` contains `25-the-rfid-door-lock.html`. The dashboard’s `fetch()` cannot load `data/lessons.json` through a `file://` origin in Chromium, so no misleading dashboard browser pass is claimed.

## Limitations

This review checks source alignment, code text, local asset presence, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, a particular RC522 breakout, LCD1602/I2C backpack/address/contrast, servo lead order or current draw, breadboard wiring, SPI/I2C signal integrity, servo movement, library installation, Arduino compilation/upload, tag detection, LCD output, or Serial Monitor output. `arduino-cli` was not available in the project environment, so no compile/upload test was run. RC522 readers, tags, LCD backpacks, servos, and Uno-compatible boards vary; learners must use their exact module documentation, keep the servo unloaded with only a paper pointer, and use only tags they own or are authorized to use in a lab. This is a bench/lab status simulation, not security guidance or an access-control design.
