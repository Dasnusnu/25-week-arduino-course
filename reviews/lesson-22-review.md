# Lesson 22 review — The Card Scanner

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/22-the-card-scanner.html`
- Local reference asset: `web/assets/lesson-22/lesson-22-mit-rfid-wiring-table.png`
- Lesson-directory route: `web/app.js`
- Focused static contract: `tests/test_lesson_22.py`

## Reference validation

Primary retained source: `sources/rfid-door-lock-mit/`, an MIT-licensed repository retained locally and not modified. The public primary reference checked was [RFID-Based Smart Door Lock System](https://github.com/mithra1x/RFID-based-Smart-Door-Lock-System), especially its README wiring table and [`main.cpp`](https://github.com/mithra1x/RFID-based-Smart-Door-Lock-System/blob/main/main.cpp). The retained README lines 30–40 and `main.cpp` lines 1–2, 7–9, 17–20, 31–33, 36–45, and 63 were compared with the page. The compatible public [MFRC522 library](https://github.com/miguelbalboa/rfid) and its [DumpInfo example](https://github.com/miguelbalboa/rfid/blob/master/examples/DumpInfo/DumpInfo.ino) were checked for SPI-based reader scope and the scan/UID/halt flow. The actual public pages are linked in the lesson section titled exactly **Reference pages**.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| Uno RC522 wiring is SDA/SS D10, SCK D13, MOSI D11, MISO D12, RST D9, GND GND, and 3.3V 3.3V | Retained README lines 30–40; public README wiring table | Pass |
| Source initializes SPI then `MFRC522(10, 9)` and `PCD_Init()` | Retained `main.cpp` lines 1–2 and 7–20 | Pass |
| A scan requires `PICC_IsNewCardPresent()` then `PICC_ReadCardSerial()` | Retained `main.cpp` lines 31–33; MFRC522 DumpInfo example | Pass |
| UID bytes are available through `rfid.uid.uidByte`, and a finished scan calls `PICC_HaltA()` | Retained `main.cpp` lines 36–45 and 63; MFRC522 DumpInfo example | Pass |
| The source integrates a servo and LCD after access comparison, but Week 22 must only scan | Retained README lines 42–53 and `main.cpp` lines 47–62; those portions are deliberately excluded | Pass |
| Library/reader use is SPI-based and reader/tag quality and capabilities vary | MFRC522 README public documentation, supported functions and limitations | Pass |

The lesson gives the exact source wiring, makes explicit that the breakout’s `SDA` label is SPI select rather than Uno I²C SDA, and labels its new sketch as a read-only UID viewer. The sketch does not call card-authentication, block-read, block-write, UID-changing, servo, LCD, relay, or access-decision APIs. It makes no security claim: it explains that a UID is an identifier, not a password or reliable access-control check. It limits use to user-owned/lab tags and explicitly prohibits cloning, writing, altering, bypassing, unlocking, or testing other access credentials.

## Attribution and image handling

- `lesson-22-mit-rfid-wiring-table.png` is a non-generated, unchanged 1000 × 700 PNG capture of the public `mithra1x/RFID-based-Smart-Door-Lock-System` GitHub repository page, captured with Chromium on 2026-10-03; SHA-256: `22f245b719c6b948e232c01667efc9911382fc297705ad7622276ea0617dcd6a`.
- The visible source capture identifies `mithra1x / RFID-based-Smart-Door-Lock-System`, marks the repository public, and visibly presents its `MIT license` tab and RC522/Uno project context. The nearby lesson caption calls it unchanged, attributes it to mithra1x, links its MIT License and bottom reference section, and does not imply the capture itself is a custom wiring diagram.
- The exact wiring table is linked from the public README in Reference pages and is reproduced as original, accessible text in the learner steps only after source validation.
- `sources/` was not changed.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_22.py -v` initially failed as expected because the Week 22 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_22.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **44 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/22-the-card-scanner.html`:
  - heading rendered as “The Card Scanner”; the local attributed image loaded (`complete: true`, natural size `1000 × 700`); the “Reference pages” heading rendered; and five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, a particular RC522 breakout, its 3.3 V regulator/level compatibility, header-label accuracy, antenna range, a card/fob, breadboard wiring, SPI signal integrity, Arduino library installation, Arduino compilation/upload, Serial Monitor output, or any observed UID. `arduino-cli` is not installed in the project environment, so no compile/upload test was run. MFRC522 breakouts and RFID tags vary; learners must use their exact module documentation and only user-owned/lab tags with permission. The source door-lock project is a learning reference, not security guidance; this lesson intentionally stays at non-authorizing UID display.
