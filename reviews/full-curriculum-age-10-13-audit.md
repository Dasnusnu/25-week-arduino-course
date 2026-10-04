# Full curriculum audit — guided ages 10–13

**Scope:** Review only of the 25 published HTML lessons in `web/lessons/`, their visible `Reference pages` sections, and `reviews/lesson-01-review.md` through `reviews/lesson-25-review.md`.

**Audience standard:** A learner aged 10–13 works with a supervising adult, uses an Uno-compatible board and the named kit parts, and can stop rather than improvise when a part differs. This audit evaluates whether that learner can make safe, observable progress without guessing. It is not physical-hardware validation.

## Executive summary

The sequence is unusually strong for a guided beginner curriculum: it moves from a one-LED circuit to more complex input, display, motor, IR, and RFID demonstrations; consistently names pins and expected observations; and keeps USB/low-voltage, permission, and no-improvisation boundaries visible. The later RFID work correctly changes an upstream door-lock example into read-only or notice-only lab demonstrations.

**Result: 20 PASS, 5 NEEDS REVISION, 0 BLOCKER.**

The revisions are tightly scoped to learner support rather than technical-source correction. They concern (1) an all-at-once, 21-wire Week 8 build, (2) how a child can positively identify the unusual 10 MΩ part in Week 10, and (3) explicit adult handling of coin cells in Weeks 19–21. The sampled public sources align with the stated source-derived pin and project claims: Freenove’s LED, digital-display, and IR tutorials; Erriez’s DS1302 library; and mithra1x’s public RC522/LCD/servo tables. The actual source URLs remain linked in each lesson’s **Reference pages** section.

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
| 08 — The Counting Machine | NEEDS REVISION | See revision finding 1. |
| 09 — The Room Thermometer | PASS | Correctly separates bare four-pin DHT11 from three-pin modules, gives face-forward pin identification, and defines useful error output. |
| 10 — The Water Detector | NEEDS REVISION | See revision finding 2. |
| 11 — Words on a Real Screen | PASS | Clearly distinguishes the four-pin I2C backpack from a bare LCD and explains A4/A5 versus duplicate SDA/SCL pins. |
| 12 — The Secret Password Pad | PASS | Explicitly frames the build as a password game, not security; the unloaded-servo and no-door boundaries are age-appropriate. |
| 13 — The Game-Style Joystick | PASS | Labels the five-module-pin prerequisite, calibrates the starting point, and makes reversed directions a code-label issue rather than a rewiring guess. |
| 14 — The Clap Trigger | PASS | Accurately presents DO as a threshold event rather than a sound meter and safely teaches small trimmer adjustments. |
| 15 — More Lights Than Pins | PASS | A complex build, but it uses source-specific pin mapping, individual resistors, and an observable travelling-light test. |
| 16 — Small Board, Big Switch | PASS | Separates the two-AA motor path from Arduino control and strongly excludes mains, unknown loads, and powered troubleshooting. |
| 17 — The Precision Spinner | PASS | Uses only the matching driver/motor, explicit IN1–IN4 labels, and clear shaft/pinch/hot-part stop conditions. |
| 18 — Point It Anywhere | PASS | Distinguishes an unloaded kit servo from a power design and gives appropriate pin, horn-clearance, and power-limit wording. |
| 19 — A Clock That Never Forgets | NEEDS REVISION | See revision finding 3. |
| 20 — Control It by Remote | NEEDS REVISION | See revision finding 4. |
| 21 — The Remote-Controlled Lamp | NEEDS REVISION | See revision finding 5. |
| 22 — The Card Scanner | PASS | Strong 3.3 V-only and permission boundary; labels RC522 SDA as SPI select, not I2C SDA, and excludes writing/cloning/access decisions. |
| 23 — Green Light, Red Light | PASS | Makes the new two-LED layout unambiguous, preserves one resistor per branch, and explicitly excludes access-control meaning. |
| 24 — The Access System | PASS | The RC522/LCD combination is clearly notice-only, with distinct SPI/I2C SDA labels and no UID decision or actuator path. |
| 25 — The RFID Door Lock | PASS | The title is counterbalanced by repeated bench-demo/no-security wording, a light paper pointer only, and clear limits on tags and hardware. |

## Blocker

None found. No reviewed lesson directs a learner toward mains power, an unknown voltage, an unprotected LED, direct motor/relay drive from an Arduino pin, or real access-control use. The high-risk topics have explicit stop conditions and exclusions.

## Needs revision

### 1. Lesson 08 — The Counting Machine

**Location:** `web/lessons/08-the-counting-machine.html`, Step 3, excerpt: “Then follow the source image exactly from the 74HC595’s Q0–Q7 outputs to the display’s eight shared cathode/segment paths.” Step 4 immediately adds four digit-select wires, and the parts list specifies 21 jumpers.

**Why this needs revision:** This is the course’s first high-density wiring task. A guided child can follow the map, but the lesson asks for twelve display-related connections across two long steps and offers no intermediate, visible check until after the full sketch is uploaded. A single crossed wire can make the final symptom look like a code problem, which encourages guessing.

**Recommended replacement wording:** Replace the final two sentences of Step 3 and the first sentence of Step 4 with:

> “Make one shared segment route at a time: source Q0 to its named display segment through one 220 Ω resistor, then mark that route on the printed diagram before starting Q1. After all eight routes are complete, ask your supervising adult to compare the eight source labels and resistor positions with you while USB is still unplugged. Only then add the four common-anode digit-select wires in the source order: D7, D6, D5, D4. Keep a paper checklist of `Q0–Q7` and `D7–D4`; do not power the display until all twelve boxes are checked.”

Also add a pre-upload success condition after Step 4: “The board is still unplugged; every display route has one resistor; and no display leg is being identified only by its physical position.”

### 2. Lesson 10 — The Water Detector

**Location:** `web/lessons/10-the-water-detector.html`, Step 3, excerpt: “use the resistor’s markings or a meter rather than guessing by color alone.”

**Why this needs revision:** A 10 MΩ resistor is uncommon in beginner kits and ordinary color bands are difficult for this age group to read reliably. “A meter” is an undeclared tool and not all inexpensive meters can confirm a 10 MΩ part accurately. The current instruction correctly says not to guess but does not give the child a supported stop-and-get-help route.

**Recommended replacement wording:** Replace the last sentence with:

> “A 10 MΩ resistor is not the same as the common 220 Ω, 1 kΩ, or 10 kΩ kit resistors. Ask your supervising adult to confirm the part from the labeled kit bag, a parts list, or a meter that has a 10 MΩ range. If you cannot positively identify a 10 MΩ resistor, stop here and do not power or substitute a resistor.”

Add this line to **Gather the parts**: “A supervising adult needs to help identify the 10 MΩ resistor from the kit label or a suitable meter.”

### 3. Lesson 19 — A Clock That Never Forgets

**Location:** `web/lessons/19-a-clock-that-never-forgets.html`, **Gather the parts**, excerpt: “The exact backup battery specified for that module, only if its maker says it is required.” The following safety paragraph says, “Coin cells can be swallowed … keep them away from children and pets.”

**Why this needs revision:** The target learners are themselves children. The warning correctly states the danger, but “keep them away from children” is not an actionable responsibility assignment for a 10–13-year-old handling the kit.

**Recommended replacement wording:** Replace the battery part-list item and first coin-cell sentence with:

> “An adult may install the exact backup battery only if the module maker says this module needs one. Do not handle, insert, remove, or test a coin cell yourself.”
>
> “A coin cell can cause severe injury if swallowed. Your supervising adult must keep it secured and out of reach of younger children and pets.”

### 4. Lesson 20 — Control It by Remote

**Location:** `web/lessons/20-control-it-by-remote.html`, **Gather the parts**, excerpt: “Infrared remote and the battery type marked on its holder,” followed by “A remote’s coin cell can be swallowed … keep it away from children and pets.”

**Why this needs revision:** This repeats the same audience mismatch. The remote is safe to use, but a child should not be implicitly asked to open the holder or handle the coin cell to identify/replace it.

**Recommended replacement wording:** Replace the remote bullet and coin-cell sentence with:

> “Infrared remote; if it needs a battery check or replacement, ask your supervising adult to read the holder and handle the coin cell.”
>
> “Do not open the battery holder or handle the coin cell yourself. A supervising adult must keep coin cells secured and out of reach of younger children and pets.”

### 5. Lesson 21 — The Remote-Controlled Lamp

**Location:** `web/lessons/21-the-remote-controlled-lamp.html`, **Gather the parts**, excerpt: “Infrared remote and its correctly identified battery,” and safety boundary, excerpt: “Keep remote coin cells away from children and pets.”

**Why this needs revision:** The learner is asked to carry forward Week 20’s remote but the same child-handling ambiguity remains. A child may assume “correctly identified” means they should open the holder.

**Recommended replacement wording:** Replace the remote bullet and coin-cell sentence with:

> “Infrared remote; its coin cell is checked or replaced only by a supervising adult.”
>
> “Do not open the remote’s battery holder or touch a loose coin cell. A supervising adult must secure coin cells away from younger children and pets.”

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
