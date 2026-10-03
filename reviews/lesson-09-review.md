# Lesson 09 review — The Room Thermometer

**Status:** PASS — ready for independent review

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/09-the-room-thermometer.html`
- Curriculum-card link: `web/app.js`
- Per-lesson checklist storage: `web/lesson.js`
- Reference image: `web/assets/lesson-09/lesson-09-dht11-hardware-connection.jpg`
- Focused contract test: `tests/test_lesson_09.py`

## Reference validation

Primary reference: `sources/freenove-ultimate-starter-kit/Tutorial.pdf`, Chapter 22, Project 22.1 “Temperature & Humidity Sensor,” PDF pages 199–203 / printed pages 195–199. The checked direct official page is [Freenove Chapter 22: Temperature & Humidity Sensor](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/22_Temperature%26Humidity.html). The local reference sketch is `sources/freenove-ultimate-starter-kit/Sketches/Sketch_22.1.1_Temperature_and_Humidity_Sensor/Sketch_22.1.1_Temperature_and_Humidity_Sensor.ino`, lines 9–41.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| Project 22.1 needs a control board, breadboard, USB cable, DHT11, one 10 kΩ resistor, and three M/M jumpers | Project 22.1 component list, PDF page 199 / printed page 195; official component-list section | Pass |
| The bare DHT11 face-forward pin labels are 1 VCC, 2 SDA, 3 NC, and 4 GND | Project 22.1 DHT11 diagram, PDF page 200 / printed page 196; official component-knowledge section | Pass |
| The source circuit routes VCC to 5 V, GND to GND, SDA to pin 10, and a 10 kΩ resistor from SDA to 5 V; NC is unused | Project 22.1 schematic/hardware connection, PDF pages 200–201 / printed pages 196–197; official circuit section | Pass |
| The exact supplied DHT library is installed from `DHT.zip` and included as `dht.h` | Project 22.1 sketch setup, PDF page 201 / printed page 197; official sketch section | Pass |
| The sketch initializes serial at 9600 baud and reads `DHT.read11(dhtPin)` with `dhtPin = 10` | Local source sketch lines 12–16 and 20–21; official sketch | Pass |
| A successful read prints `DHT.humidity` and `DHT.temperature`; checksum, timeout, and unknown statuses are handled | Local source sketch lines 22–39; official sketch/error explanation | Pass |
| Reads are spaced by one second | Local source sketch line 41; official sketch | Pass |
| Lesson wording and troubleshooting are original while preserving the validated wiring, library API, pin assignment, status checks, and cadence | Original lesson compared against cited source | Pass — intentional original implementation |

## Attribution and source handling

- The lesson includes an unchanged rasterization of the permitted source-pack PDF page containing Project 22.1’s hardware connection, with visible Chapter/page attribution.
- The page names Freenove, has the required `Reference pages` heading, links the direct Chapter 22 page and upstream license declaration, and links CC BY-NC-SA 3.0.
- The source pack was not modified. No generated image or additional third-party source pack was added.
- The local upstream `readme.md` declares CC BY-NC-SA 3.0 at line 64.

## Interactive verification

- Red test first: `python3 -m unittest tests/test_lesson_09.py` → **2 failures** before the page and image existed, as expected.
- Focused static contract test: `python3 -m unittest tests/test_lesson_09.py` → **2 passed**.
- Full static test suite: `python3 -m unittest discover -s tests -p 'test_*.py' -v` → **18 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- JPEG verification: Pillow opened and verified `lesson-09-dht11-hardware-connection.jpg` at **1241 × 1754**.
- Browser test using `http://127.0.0.1:8765/lessons/09-the-room-thermometer.html`:
  - the reference image loaded successfully (`complete: true`, natural width `1241`);
  - five checklist controls and `Reference pages` rendered; initial progress read `0 of 5 checks complete.`;
  - a visible click on the first checkbox updated progress to `1 of 5 checks complete.` and the progress element value to `1`;
  - a visible click on `Reset this lesson’s checks` returned progress to `0 of 5 checks complete.`, cleared every checkbox, and stored `[]` under the lesson-specific localStorage key.

## Limitations

This review validates the lesson against Freenove’s reference materials, its static contract, and browser behavior. It does **not** electrically test a physical Uno-compatible board, DHT11, breadboard wiring, resistor value, installed library, Serial Monitor output, or uploaded sketch. Before USB power is connected, verify the target sensor’s face-forward pin labels and every breadboard row against the source image.
