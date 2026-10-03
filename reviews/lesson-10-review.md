# Lesson 10 review — The Water Detector

**Status:** PASS — corrected reference-image gate complete

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/10-the-water-detector.html`
- Local Keyestudio comparison assets: `web/assets/lesson-10/lesson-10-keyestudio-water-level-sensor.png` and `web/assets/lesson-10/lesson-10-keyestudio-water-level-alarm-circuit.png`
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

## Attribution and image handling

- The lesson now displays two local, non-generated Keyestudio reference images: the exposed-trace water sensor and the Project 10 controller/buzzer connection diagram. Both are exact local downloads of the source-page images, are visually attributed to Keyestudio in their captions, and have descriptive alternative text.
- Source page: [Keyestudio Project 10 Water Level Alarm](https://docs.keyestudio.com/projects/KS0158/en/latest/docs/2.%20Arduino/Project/Project10.html).
- Direct image URLs: [sensor image](https://docs.keyestudio.com/projects/KS0158/en/latest/_images/image-20251127143002796.png) and [connection diagram](https://docs.keyestudio.com/projects/KS0158/en/latest/_images/image-20251127143136500.png).
- The source page identifies its design as an exposed-parallel-trace analog water sensor connected to A0 and an active buzzer on D6. The lesson labels both images as a **comparable water-level alarm reference**, explicitly states that the Keyestudio A0/D6 circuit is not used, and retains the technically distinct RBD dry foil, 10 MΩ, D2/D3 build and safety warnings.
- Reuse basis: the project operator explicitly authorized Keyestudio guide/image use with attribution. This review does not infer or claim an upstream Keyestudio license. The local retained archive `sources/keyestudio-ks0158/Arduino.7z` was reported by the operator as integrity-checked with `7z l`; it is excluded from Git and was not modified.
- The required `Reference pages` section links the actual RBD Water Sensor, RBD Capacitance, upstream MIT repository, raw calibration sketch, and Keyestudio Project 10 source page.
- `sources/` was not modified.

## Interactive verification

- Focused static contract test: `python3 -m unittest tests/test_lesson_10.py -v` → **2 passed**. The image/reference contract requires both local Keyestudio assets, their HTML references, visible Keyestudio attribution, the direct Project 10 source-page link, and the RBD-distinction warning.
- Full static test suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **20 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- Asset verification: `file web/assets/lesson-10/lesson-10-keyestudio-water-level-sensor.png web/assets/lesson-10/lesson-10-keyestudio-water-level-alarm-circuit.png` identified valid PNG images at **502 × 149** and **553 × 227**, respectively.
- Browser test using `http://127.0.0.1:8891/lessons/10-the-water-detector.html`:
  - title and heading rendered; both local images loaded (`complete: true`, natural widths `502` and `553`); their source attribution and `Reference pages` heading/link were visible;
  - five checklist controls rendered with initial progress `0 of 5 checks complete.`;
  - a visible click on the first checkbox changed progress to `1 of 5 checks complete.` and progress value to `1`;
  - a visible click on `Reset this lesson’s checks` restored `0 of 5 checks complete.`, cleared all five controls, and stored `[]` under `25week-guide:/lessons/10-the-water-detector.html:checks`.

## Limitations

This review validates source alignment, static contracts, local image loading, and browser behavior. It does **not** electrically test an Uno-compatible board, the three installed RBD libraries, a 10 MΩ resistor, foil sensor, plastic container, uploaded sketch, or Serial Monitor output. The Keyestudio visual reference is intentionally not a wiring substitute: its exposed-trace/A0/D6 alarm design is materially different from this dry RBD capacitance lesson. The source’s Water Sensor page contains the documented 1 MΩ/10 MΩ contradiction; this lesson deliberately follows the consistent 10 MΩ RBD Capacitance documentation, but a learner should not power a build when the resistor cannot be positively identified.
