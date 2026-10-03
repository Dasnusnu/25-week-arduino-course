# Lesson 14 review — The Clap Trigger

**Status:** PASS — source-validated, browser-tested; no physical hardware validation

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/14-the-clap-trigger.html`
- Local reference asset: `web/assets/lesson-14/lesson-14-ky038-wiring.webp`
- Lesson-directory route: `web/app.js`
- Curriculum coverage record: `data/lessons.json`
- Focused static contract: `tests/test_lesson_14.py`

## Reference validation

Primary public source: [Luis Llamas — Detecting sound with Arduino and KY-038 microphone](https://www.luisllamas.es/en/detect-sound-arduino-ky-038-microphone/). The page was checked in a browser. Its footer states: “Except where expressly noted, the contents of this site are provided under a Creative Commons License BY-NC-SA.” The primary image and original tutorial are therefore attributed locally as used under that documented CC BY-NC-SA notice; no licence version was inferred beyond what the source states.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| KY-038 combines a microphone with an LM393 comparator and has analog plus digital readings | Luis Llamas module description | Pass |
| DO is appropriate for threshold detection, while AO is an analog estimate rather than a calibrated sound level | Luis Llamas module description | Pass |
| Module power is 5V/GND and the digital DO path can connect to D9 | Luis Llamas wiring diagram and D9 code example | Pass |
| The sensitivity trimmer controls the digital threshold | Luis Llamas assembly guidance | Pass |
| D9 can be read with `digitalRead()` and state can be time-gated with `millis()` | Arduino language references linked in the lesson | Pass |

The learner sketch is original. It retains source-aligned D9 digital input and the built-in LED action, then adds a rising-edge condition and a 350 ms lockout so one extended comparator output is not treated as repeated switch requests. The lockout is described as noise handling, not as a source-supplied calibration or a guarantee of reliable detection. The page links actual public technical sources in a section titled exactly **Reference pages**.

## Attribution and image handling

- `lesson-14-ky038-wiring.webp` is a non-generated, unchanged 394 × 113 WebP download of Luis Llamas’s KY-038 wiring image (`arduino-microfono-montaje.webp`).
- The image visibly supports exactly the selected module and connections: VCC to 5V, GND to GND, and DO to D9.
- Its nearby caption visibly names Luis Llamas, identifies the image as unchanged, cites the source site’s CC BY-NC-SA notice, links the licence family, and points to the bottom reference section.
- `sources/` was not changed. The unused retained Keyestudio archive was inspected only to confirm it contains an analog-sensor Project 8 code path; it was not used for the finished KY-038 digital-output lesson because it lacked a ready-to-use image/licence gate.

## Interactive and static verification

- Red-first focused contract: `python3 -m unittest tests/test_lesson_14.py -v` initially failed as expected because the Week 14 page and required image did not exist.
- Focused static contract after implementation: `python3 -m unittest tests/test_lesson_14.py -v` → **2 passed**.
- Full static suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **28 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- JSON syntax: `python3 -m json.tool data/lessons.json >/dev/null` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `file:///home/jacob/projects/25week-guide/web/lessons/14-the-clap-trigger.html`:
  - heading rendered as “The Clap Trigger”; the local Luis Llamas image loaded (`complete: true`, natural size `394 × 113`); and the “Reference pages” heading rendered;
  - five checklist controls rendered at `0 of 5 checks complete.`;
  - clicking the first checkbox changed the UI to `1 of 5 checks complete.`, with progress value `1` and local storage `["1"]`;
  - clicking `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]`.
- The browser screenshot request timed out after the functional assertions had completed; it is not used as visual evidence.

## Limitations

This review checks source alignment, code text, local asset integrity, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, a particular KY-038 module, USB power, the sensitivity trimmer, any wiring, Serial Monitor, upload, actual sound detection, or LED response. `arduino-cli` was not available in the project environment, so no compile/upload test was run. Comparable-looking microphone boards can use different labels, output polarity, signal conditioning, or voltage requirements; the lesson is deliberately limited to the source-identified KY-038/LM393 board with labeled VCC/GND/DO/AO, and tells learners to use their exact board documentation when it differs. The threshold depends on room noise and adjustment, and the circuit is not suitable for security, safety, medical, metering, or mains-control use.
