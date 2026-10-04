# Lesson 24 review — The Access System

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/24-the-access-system.html`
- Reused local reference asset: `web/assets/lesson-22/lesson-22-mit-rfid-wiring-table.png`
- Lesson-directory route: `web/app.js`
- Curriculum metadata: `data/lessons.json`
- Focused static contract: `tests/test_lesson_24.py`

## Reference validation

Primary retained source: `sources/rfid-door-lock-mit/` at upstream commit `b82c0a13299f87d8540689303394beac567aa183` (`https://github.com/mithra1x/RFID-based-Smart-Door-Lock-System.git`). The local source was not modified. Its `LICENSE` is MIT (copyright 2025 Mikayıl Namazov); the public README, `main.cpp`, and license are linked from the lesson section titled exactly **Reference pages**.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| RC522/Uno wiring is SDA D10, SCK D13, MOSI D11, MISO D12, RST D9, GND GND, and 3.3V 3.3V | Retained README lines 30–40; public README wiring table | Pass |
| I2C LCD/Uno wiring is VCC 5V, GND GND, SDA A4, SCL A5 | Retained README lines 42–47; public README wiring table | Pass |
| The source initializes SPI, `MFRC522(10, 9)`, LCD `0x27` at 16×2, LCD init/backlight, and new-card/read-serial flow | Retained `main.cpp` lines 1–25 and 31–35 | Pass |
| A completed scan calls `PICC_HaltA()` | Retained `main.cpp` line 63; MFRC522 DumpInfo reference | Pass |
| The source subsequently compares a four-byte UID, presents access language, and drives an SG90 servo | Retained `main.cpp` lines 38–62; retained README lines 49–53 and 76–90 | Pass — deliberately excluded |

The lesson makes no authorization or identity claim. Its original sketch observes a nearby user-owned/lab tag, displays `Tag seen` and `Lab demo only`, then returns to a waiting message. It contains no stored UID, UID comparison, allow list, card-memory operation, cloned/written credential operation, servo/relay/actuator import or pin, lock/door command, “Access Granted,” or “Access Denied” behavior. Learner text explicitly prohibits cloning, writing, altering, bypassing, unlocking, testing credentials, access decisions, and connection to real locking hardware.

## Attribution and image handling

- `lesson-22-mit-rfid-wiring-table.png` is a retained, non-generated, unchanged 1000 × 700 PNG capture of the public `mithra1x/RFID-based-Smart-Door-Lock-System` repository page. It is reused here with a visible caption naming mithra1x, the repository, the MIT License, the unchanged status, and the Reference pages section.
- The image is a source-context capture rather than an asserted custom wiring diagram. Exact RC522 and LCD paths are presented as accessible text only after comparison with retained README lines 30–47.
- `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_24.py -v` initially failed as expected because the Week 24 page did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_24.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **48 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/24-the-access-system.html`:
  - heading rendered as “The Access System”; “Reference pages” rendered; the attributed local image loaded (`complete: true`, natural size `1000 × 700`); and five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`.

## Limitations

This review checks source alignment, code text, local asset presence, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, a particular RC522 breakout, a specific LCD1602/I2C backpack or its contrast/address, breadboard wiring, SPI/I2C signal integrity, library installation, Arduino compilation/upload, tag detection, LCD output, or Serial Monitor output. `arduino-cli` is not installed in the project environment, so no compile/upload test was run. RC522 readers, RFID tags, LCD backpacks, and Uno-compatible boards vary; learners must use their exact module documentation and only tags they own or are authorized to use in a lab. This lesson is a status/output simulation and is not security guidance or an access-control design.
