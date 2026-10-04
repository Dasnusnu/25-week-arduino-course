# Full curriculum audit — guided ages 10–13

**Scope:** Review only of the 25 published HTML lessons in `web/lessons/`, their visible `Reference pages` sections, and `reviews/lesson-01-review.md` through `reviews/lesson-25-review.md`.

**Audience standard:** A learner aged 10–13 works with a supervising adult, uses an Uno-compatible board and the named kit parts, and can stop rather than improvise when a part differs. This audit evaluates whether that learner can make safe, observable progress without guessing. It is not physical-hardware validation.

## Executive summary

The sequence is unusually strong for a guided beginner curriculum: it moves from a one-LED circuit to more complex input, display, motor, IR, and RFID demonstrations; consistently names pins and expected observations; and keeps USB/low-voltage, permission, and no-improvisation boundaries visible. The later RFID work correctly changes an upstream door-lock example into read-only or notice-only lab demonstrations.

**Result: 25 PASS, 0 NEEDS REVISION, 0 BLOCKER.**

The two learner-support revisions identified in the first audit pass are resolved: Week 08 now requires unplugged, route-by-route Q0–Q7/D7–D4 checking with adult comparison, and Week 10 gives an adult-assisted 10 MΩ identification and no-substitution stop condition. These changes are recorded in the focused commit `fix: clarify guided wiring checks for lessons 08 and 10`. Battery handling is outside this age-appropriateness audit: the project operator has chosen to assume these learners can safely handle ordinary battery-related tasks. The sampled public sources align with the stated source-derived pin and project claims: Freenove’s LED, digital-display, and IR tutorials; Erriez’s DS1302 library; and mithra1x’s public RC522/LCD/servo tables. The actual source URLs remain linked in each lesson’s **Reference pages** section.

## Per-lesson result

| Lesson | Result | Age-10–13 review note |
|---|---|---|
| 01 — Light Your First LED | PASS | Clear LED polarity, series-resistor, pin-13, unplug-before-rewire sequence, observable blink, and troubleshooting. |
| 02 — Make Some Noise | PASS | Distinguishes active from passive buzzer and directs the learner to match an uncertain transistor to the visual reference instead of guessing. |
| 03 — The Melody Machine | PASS | Builds directly on Lesson 2, defines passive-buzzer behavior, and gives a safe, observable sound result. |
| 04 — The Control Knob | PASS | Explains the wiper and A0 with a bounded, low-voltage build and realistic near-endpoint expectation. |
| 05 — The Darkness Detector | PASS | The sensor junction is explicitly traced; LED safety and light-testing guidance are clear. |
| 06 — Mix Your Own Colours | PASS | Correctly stops a learner with a common-cathode or unknown RGB LED and keeps each LED path independently protected. |
| 07 — Make Numbers Appear | PASS | Dense but suitable with supervision: it names every 74HC595 control/power pin, requires the source-specific display map, and gives a safe unplug-first fault path. |
| 08 — The Counting Machine | PASS | Unplugged, route-by-route Q0–Q7 and D7–D4 checklist, adult label/resistor comparison, and pre-power success condition remove the high-density-wiring guess path. |
| 09 — The Room Thermometer | PASS | Correctly separates bare four-pin DHT11 from three-pin modules, gives face-forward pin identification, and defines useful error output. |
| 10 — The Water Detector | PASS | Parts list and wiring step require adult positive identification of 10 MΩ and a no-power/no-substitution stop condition when it cannot be identified. |
| 11 — Words on a Real Screen | PASS | Clearly distinguishes the four-pin I2C backpack from a bare LCD and explains A4/A5 versus duplicate SDA/SCL pins. |
| 12 — The Secret Password Pad | PASS | Explicitly frames the build as a password game, not security; the unloaded-servo and no-door boundaries are age-appropriate. |
| 13 — The Game-Style Joystick | PASS | Labels the five-module-pin prerequisite, calibrates the starting point, and makes reversed directions a code-label issue rather than a rewiring guess. |
| 14 — The Clap Trigger | PASS | Accurately presents DO as a threshold event rather than a sound meter and safely teaches small trimmer adjustments. |
| 15 — More Lights Than Pins | PASS | A complex build, but it uses source-specific pin mapping, individual resistors, and an observable travelling-light test. |
| 16 — Small Board, Big Switch | PASS | Separates the two-AA motor path from Arduino control and strongly excludes mains, unknown loads, and powered troubleshooting. |
| 17 — The Precision Spinner | PASS | Uses only the matching driver/motor, explicit IN1–IN4 labels, and clear shaft/pinch/hot-part stop conditions. |
| 18 — Point It Anywhere | PASS | Distinguishes an unloaded kit servo from a power design and gives appropriate pin, horn-clearance, and power-limit wording. |
| 19 — A Clock That Never Forgets | PASS | Clear DS1302 wiring and backup-battery boundaries for the selected module. |
| 20 — Control It by Remote | PASS | Clear IR wiring, decode workflow, and remote handling guidance. |
| 21 — The Remote-Controlled Lamp | PASS | Clear low-voltage LED/IR integration and explicit no-mains boundary. |
| 22 — The Card Scanner | PASS | Strong 3.3 V-only and permission boundary; labels RC522 SDA as SPI select, not I2C SDA, and excludes writing/cloning/access decisions. |
| 23 — Green Light, Red Light | PASS | Makes the new two-LED layout unambiguous, preserves one resistor per branch, and explicitly excludes access-control meaning. |
| 24 — The Access System | PASS | The RC522/LCD combination is clearly notice-only, with distinct SPI/I2C SDA labels and no UID decision or actuator path. |
| 25 — The RFID Door Lock | PASS | The title is counterbalanced by repeated bench-demo/no-security wording, a light paper pointer only, and clear limits on tags and hardware. |

## Blocker

None found. No reviewed lesson directs a learner toward mains power, an unknown voltage, an unprotected LED, direct motor/relay drive from an Arduino pin, or real access-control use. The high-risk topics have explicit stop conditions and exclusions.

## Resolved findings

### 1. Lesson 08 — The Counting Machine — RESOLVED

**Location:** `web/lessons/08-the-counting-machine.html`, Step 3, excerpt: “Then follow the source image exactly from the 74HC595’s Q0–Q7 outputs to the display’s eight shared cathode/segment paths.” Step 4 immediately adds four digit-select wires, and the parts list specifies 21 jumpers.

**Resolution:** The final Step 3 guidance now has the learner build and mark one Q0–Q7 route at a time, then compare all eight source labels and resistor positions with a supervising adult while USB remains unplugged. Step 4 adds the Q0–Q7/D7–D4 paper checklist and requires confirmation that every display route has one resistor and no leg was identified only by physical position. Focused contract and browser checks passed; evidence is the focused commit `fix: clarify guided wiring checks for lessons 08 and 10`.

**Recommended replacement wording:** Replace the final two sentences of Step 3 and the first sentence of Step 4 with:

> “Make one shared segment route at a time: source Q0 to its named display segment through one 220 Ω resistor, then mark that route on the printed diagram before starting Q1. After all eight routes are complete, ask your supervising adult to compare the eight source labels and resistor positions with you while USB is still unplugged. Only then add the four common-anode digit-select wires in the source order: D7, D6, D5, D4. Keep a paper checklist of `Q0–Q7` and `D7–D4`; do not power the display until all twelve boxes are checked.”

Also add a pre-upload success condition after Step 4: “The board is still unplugged; every display route has one resistor; and no display leg is being identified only by its physical position.”

### 2. Lesson 10 — The Water Detector — RESOLVED

**Location:** `web/lessons/10-the-water-detector.html`, Step 3, excerpt: “use the resistor’s markings or a meter rather than guessing by color alone.”

**Resolution:** The parts list now requires supervising-adult assistance to identify the 10 MΩ resistor from a labeled kit bag or suitable meter. Step 3 explains that it differs from common 220 Ω, 1 kΩ, and 10 kΩ parts, gives the supported confirmation paths, and says to stop without power or substitution if it cannot be positively identified. Focused contract and browser checks passed; evidence is the focused commit `fix: clarify guided wiring checks for lessons 08 and 10`.

**Recommended replacement wording:** Replace the last sentence with:

> “A 10 MΩ resistor is not the same as the common 220 Ω, 1 kΩ, or 10 kΩ kit resistors. Ask your supervising adult to confirm the part from the labeled kit bag, a parts list, or a meter that has a 10 MΩ range. If you cannot positively identify a 10 MΩ resistor, stop here and do not power or substitute a resistor.”

Add this line to **Gather the parts**: “A supervising adult needs to help identify the 10 MΩ resistor from the kit label or a suitable meter.”

## Nice-to-have

### Review-record consistency

Lessons 01–10 have review records with source and browser/static evidence, but their limitation language is not standardized with the explicit “no physical hardware validation” wording used in Lessons 11–25. This does not change a lesson result and is not a content defect.

**Recommended wording for future record maintenance:**

> “This review validates source alignment, static checks, and browser behavior. It does not include physical hardware assembly, electrical measurement, Arduino compilation/upload, or observed device behavior.”

## Source and reference-page alignment checked

- Every published lesson contains a visible heading titled exactly **Reference pages** and public source links. The 25 focused static lesson tests passed, including their reference/image contracts.
- Sampled public source checks confirmed the source relationships used by the lessons: Freenove’s LED page names the board, breadboard, LED, 220 Ω resistor, and USB setup; its Digital Display page documents the common-anode display, 74HC595, eight 220 Ω resistors, and the cited digit encodings; and its IR page documents the D12 receiver circuit and 10 kΩ pull-up. Erriez documents the DS1302 as a three-wire RTC library. The public mithra1x repository publishes the same RC522-to-Uno, LCD-to-Uno, and servo-to-Uno pin tables cited by Lessons 22, 24, and 25.
- The lesson text’s source-specific constraints are aligned with those pages: common-anode display warnings in Lessons 7–8, Uno/D12 IR receiver wiring in Lessons 20–21, DS1302 D2/D3/D4 mapping in Lesson 19, and RC522 3.3 V plus D10/D13/D11/D12/D9 wiring in Lessons 22, 24, and 25.

## Audit limitations

This is a content, source-alignment, and guided-learner review. It does not electrically test any lesson, part variant, uploaded sketch, library version, source-pack image, Arduino compilation, or real RFID/IR/servo/motor behavior. It makes no claim of physical hardware validation.
