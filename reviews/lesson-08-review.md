# Lesson 08 review — The Counting Machine

**Status:** PASS — ready for independent review

**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/08-the-counting-machine.html`
- Curriculum-card link: `web/app.js`
- Per-lesson checklist storage: `web/lesson.js`
- Reference image: `web/assets/lesson-08/lesson-08-four-digit-seven-segment-circuit.jpg`
- Focused contract test: `tests/test_lesson_08.py`

## Reference validation

Primary reference: `sources/freenove-ultimate-starter-kit/Tutorial.pdf`, Chapter 17, Project 17.2 “4-digit 7-segment Display,” PDF pages 162–169 / printed pages 158–165. The checked upstream public page is [Freenove Chapter 17: Digital Display, Project 17.2](https://docs.freenove.com/projects/fnk0017/en/latest/fnk0017/codes/tutorial/17_Digital_Display.html#project-4-digit-7-segment-display). The local reference sketches are `sources/freenove-ultimate-starter-kit/Sketches/Sketch_17.2.1_4_Digit_7-Segment_Display/Sketch_17.2.1_4_Digit_7-Segment_Display.ino`, lines 9–55, and `Sketch_17.2.2_4_Digit_7-Segment_Display/Sketch_17.2.2_4_Digit_7-Segment_Display.ino`, lines 11–72.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| The project uses a board, USB cable, breadboard, 74HC595, one 4-digit display, eight 220 Ω resistors, and 21 jumpers | Project 17.2 component list, PDF page 162 / printed page 158; official component-list section | Pass |
| The kit display is common-anode with shared cathode paths and four digit-select common ports | Project 17.2 component-knowledge text and diagrams, PDF page 163 / printed page 159; official component-knowledge section | Pass |
| Arduino pins 11, 13, and 12 go to 74HC595 DS pin 14, SH_CP pin 11, and ST_CP pin 12 | Project 17.2 circuit/hardware connection, PDF pages 164–165 / printed pages 160–161; local sketches lines 9–11 and 11–13 | Pass |
| Arduino pins 7, 6, 5, and 4 select the four common-anode digit ports | Project 17.2 circuit statement, PDF page 164 / printed page 160; local sketches line 12 and line 14 | Pass |
| The 74HC595 needs VCC pin 16 and MR pin 10 at 5 V, plus GND pin 8 and OE pin 13 at GND | Project 17.2 hardware-connection image, PDF page 165 / printed page 161 | Pass |
| Each Q0–Q7 output reaches a shared segment path through its own 220 Ω resistor | Project 17.2 hardware-connection image, PDF page 165 / printed page 161 | Pass |
| Common-anode encodings 0–9 are `0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90` | Local sketches line 15 and line 19; official sketch table | Pass |
| A digit scan disables all common pins, enables one, shifts data least-significant-bit first, dwells 5 ms, then writes `0xff` to blank it | Local Sketch 17.2.1 lines 27–55 and Sketch 17.2.2 lines 41–72; official explanation of scanning and ghosting | Pass |
| The original lesson uses `millis()` rather than Freenove’s optional `FlexiTimer2` counter but preserves the validated display wiring, encodings, scan order, dwell, and blanking behavior | Original lesson code; source Sketch 17.2.2 uses a one-second timer only to increase its counter | Pass — intentional original implementation |

## Attribution and source handling

- The lesson includes an unchanged rasterization of the permitted source-pack PDF page containing Project 17.2’s hardware connection, with visible Chapter/page attribution.
- The page names Freenove, links the direct official Project 17.2 page and tutorial index under the required `Reference pages` heading, and links CC BY-NC-SA 3.0.
- The source pack was not modified. No generated image or third-party source pack was added.

## Interactive verification

- Red test first: `python -m unittest tests/test_lesson_08.py -v` → **2 failures** before the page and image existed, as expected.
- Focused static contract test: `python -m unittest tests/test_lesson_08.py -v` → **2 passed**.
- Full static test suite: `python -m unittest discover -s tests -v` → **16 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Diff hygiene: `git diff --check` → **passed**.
- JPEG verification: Pillow opened and verified `lesson-08-four-digit-seven-segment-circuit.jpg` at **1241 × 1754**.
- Browser test using the local Week 08 lesson file:
  - the reference image loaded successfully (`complete: true`, natural size `1241 × 1754`);
  - five checklist controls rendered and initial progress read `0 of 5 checks complete.`;
  - a real visible checkbox click updated progress to `1 of 5 checks complete.` and stored `["1"]` under the lesson-specific key;
  - a real visible reset-button click returned progress to `0 of 5 checks complete.`, cleared all controls, and stored `[]`;
  - the `Reference pages` section rendered with the direct official Project 17.2 and tutorial-index links.

## Limitations

This review validates the lesson against Freenove’s reference materials and browser behavior. It does **not** electrically test a physical Uno-compatible board, 74HC595, display pinout/type, resistor values, or uploaded sketch. Before USB power is connected, verify the target kit’s display part/pin designations and every breadboard row against the source image.
