# Lesson 01 review — Light Your First LED

**Status:** PASS — ready for user review  
**Reviewed:** 2026-10-03

## Scope checked

- Original interactive lesson: `web/lessons/01-light-your-first-led.html`
- Interactive checklist behavior: `web/lesson.js`
- Reference images:
  - `web/assets/lesson-01/lesson-01-components.jpg`
  - `web/assets/lesson-01/lesson-01-wiring.jpg`

## Reference validation

Primary reference: `sources/freenove-ultimate-starter-kit/Tutorial.pdf`, Chapter 1, Project 1.2 “Control LED with Control Board”.

| Lesson claim | Reference evidence | Result |
|---|---|---|
| Build uses an Uno-compatible board, breadboard, USB cable, LED, 220 Ω resistor, and jumper wires | Project 1.2 follows the Chapter 1 component list; the source component image is retained in this project | Pass |
| Circuit is pin 13 → 220 Ω resistor → LED → GND | Tutorial PDF printed page 20 (rendered from PDF page 24) schematic and hardware drawing | Pass |
| Pin 13 is configured as an output and alternates HIGH/LOW every 1000 ms | `Sketches/Sketch_1.2.1_Control_LED_by_Control_Board/Sketch_1.2.1_Control_LED_by_Control_Board.ino`, lines 9–21 | Pass |
| LED is installed across separate breadboard rows and must be checked while USB is disconnected | Tutorial’s hardware-connection guidance and its warning to connect USB after checking connections | Pass |

## Interactive verification

- Static contract tests: `python3 -m unittest tests/test_lesson_01.py` → **2 passed**.
- JavaScript syntax: `node --check web/app.js` and `node --check web/lesson.js` → **passed**.
- Browser test at `http://192.168.50.24:8080/web/lessons/01-light-your-first-led.html`:
  - both reference images loaded successfully;
  - all five checklist controls rendered;
  - selecting a check updated progress from 0/5 to 1/5;
  - reset returned it to 0/5.

## Limitations

This validates the lesson against the reference materials and browser behavior. It does **not** electrically test a physical board; final hardware validation requires assembling the lesson with the target Uno-compatible kit.

## Attribution

Reference images and upstream materials are from Freenove’s Ultimate Starter Kit repository and are subject to the stated CC BY-NC-SA 3.0 terms. The lesson text is original; do not remove attribution or reuse the material commercially.
