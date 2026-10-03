# Lesson 10 review — The Water Detector

**Status:** PASS — ready for independent review

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/10-the-water-detector.html`
- Curriculum-card link: `web/app.js`
- Accessible, original text wiring map styling: `web/lesson.css`
- Focused contract test: `tests/test_lesson_10.py`

## Reference validation

Primary retained source: `sources/rbd-water-sensor-mit/` at local commit `a9da825` (RBD_WaterSensor 2.0.1, MIT). The local calibration sketch is `examples/calibrate_water_sensor/calibrate_water_sensor.ino`, lines 5–29. Public primary documentation checked: [RBD Water Sensor](http://robotsbigdata.com/docs-arduino-water-sensor.html), [RBD Capacitance](http://robotsbigdata.com/docs-arduino-capacitance.html), and the [RBD_WaterSensor upstream repository](https://github.com/alextaujenis/RBD_WaterSensor).

| Lesson claim | Reference evidence | Result |
|---|---|---|
| Sensor detects a relative capacitance change from outside a non-conductive plastic container | RBD_WaterSensor `library.properties` line 6; Water Sensor overview | Pass |
| D2 is the send pin and D3 is the receive/foil pin | Local example line 9; Water Sensor example sketch; Capacitance example wiring | Pass |
| The foil pad belongs outside a dry, watertight plastic container | Water Sensor overview and numbered example-wiring steps 3–4 | Pass |
| Use a 10 MΩ resistor between D2 and D3 | Capacitance documentation’s numbered wiring and diagram both specify 10 MΩ | Pass |
| Water Sensor documentation has an internal resistor-value conflict | Its numbered step 1 says 1 MΩ, while its reference diagram says 10 MΩ; the matching Capacitance page consistently says 10 MΩ | Disclosed; lesson follows the internally consistent Capacitance reference |
| Library constructor is `WaterSensor(2, 3, 3)` and serial speed is 115200 | Local example lines 9 and 12 | Pass |
| Calibration example uses three levels 120/154/187 and max level 220 | Local example lines 13–16 | Pass, with lesson explicitly labeling them source sample values rather than universal values |
| Continuous `update()` and `onRawValueChange()` gate the printed active-level/raw-value result | Local example lines 19–28; Water Sensor API documentation | Pass |
| Adapted code carries source and MIT attribution | Visible code comment plus reference pages link upstream repository and raw example | Pass |

## Attribution and source handling

- The required `Reference pages` section links the actual Water Sensor documentation, Capacitance documentation, upstream MIT repository, and raw calibration sketch.
- No downloaded third-party asset, source-pack file, or generated image was added. The retained MIT source repository has no circuit image, and the public documentation does not document a compatible license for its image asset.
- Instead, the lesson presents an explicitly attributed, accessible original text wiring map (`role="img"`) and links the source pages’ reference diagrams. This avoids claiming reuse rights that were not documented.
- `sources/` was not modified.

## Interactive verification

- Red test first: `python3 -m unittest tests/test_lesson_10.py` → **1 failure and 1 error** before the lesson page existed, as expected.
- Focused static contract test: `python3 -m unittest tests/test_lesson_10.py -v` → **2 passed**.
- Full static test suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **20 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Browser test at `http://127.0.0.1:8765/web/lessons/10-the-water-detector.html`:
  - page title, heading, original wiring map, four source links, five checklist controls, and `Reference pages` rendered;
  - no image asset is intentionally embedded (`document.images.length === 0`); the accessible visual rendered with the correct 10 MΩ/D2/D3 text;
  - initial progress read `0 of 5 checks complete.`;
  - a visible click on the first checkbox changed progress to `1 of 5 checks complete.` and progress value to `1`;
  - a visible click on `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]` under `25week-guide:/web/lessons/10-the-water-detector.html:checks`.

## Limitations

This review validates source alignment, static contracts, and browser behavior. It does **not** electrically test an Uno-compatible board, the three installed RBD libraries, a 10 MΩ resistor, foil sensor, plastic container, uploaded sketch, or Serial Monitor output. The source’s Water Sensor page contains the documented 1 MΩ/10 MΩ contradiction; this lesson deliberately follows the consistent 10 MΩ RBD Capacitance documentation, but a learner should not power a build when the resistor cannot be positively identified.
