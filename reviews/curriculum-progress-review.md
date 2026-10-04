# Curriculum progress and parts checklist review

## Scope

- Shared parts lists now become keyboard-accessible, one-item-per-line checklists at runtime.
- Parts state is stored separately from build-step state in browser `localStorage`.
- The dashboard displays each lesson's five-step build progress, a completed-card state at 5/5, and a 25-lesson / 125-build-check aggregate.

## Static evidence

- `tests/test_curriculum_progress.py` was introduced first and run red before the implementation. It verifies the 25 lesson-page inventory, `.parts` presence, five `data-step` checks per page, separate state keys, accessible checklist markup contracts, and dashboard hooks.
- Green verification: `python3 -m unittest tests.test_curriculum_progress` (4 tests) and `python3 -m unittest discover -s tests` (54 tests).
- JavaScript syntax and whitespace verification: `node --check web/lesson.js`, `node --check web/app.js`, and `git diff --check`.

## Browser evidence

- Local project-root preview: all 25 dashboard cards rendered. With saved checks for Week 01 (5) and Week 02 (2), the dashboard read `1 of 25 lessons complete · 7 of 125 build checks complete`; the Week 01 card read `5 of 5 build checks`, exposed the same accessible label, and received `lesson--complete`.
- Week 01 desktop: five part rows rendered as associated labels and inputs; computed grid had one column. Space toggled the focused first part checkbox, its separate `:parts` state persisted after reload, and reset cleared both parts and build-check state.
- Week 25 mobile (390 px): six parts rendered in a one-column layout with no horizontal overflow; one build check and one part check both persisted after reload.

## Limitations

- This is browser/UI validation only; no Arduino hardware was assembled or physically validated.
- Progress is intentionally based only on the five build-step checks; parts checklist state does not mark a lesson complete.
