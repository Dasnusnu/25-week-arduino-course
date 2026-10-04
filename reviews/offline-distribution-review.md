# Offline distribution review

## Scope

Portable-file hosting and packaging only: static lesson metadata, an offline launcher, quick-start instructions, and a distributable ZIP. Lesson writing, source material, and assets were not changed.

## Evidence

- `web/lessons-data.js` is generated from `data/lessons.json` by `tools/build_offline_package.py`; `web/index.html` loads it before `app.js`.
- The dashboard no longer requires a runtime network request and reports a clear curriculum-load error when local data is absent.
- `python3 tools/build_offline_package.py` regenerated `web/lessons-data.js` and `dist/25-week-arduino-guide-offline.zip`.
- `python3 -m unittest tests/test_offline_distribution.py tests/test_curriculum_progress.py` passed: 9 tests. The distribution contract compares generated metadata with the inventory, checks static script order/no request call, validates launcher/quick-start content, and inspects ZIP contents (including 25 lesson pages and excluded development/source paths).
- Chromium browser QA opened `file:///home/jacob/projects/25week-guide/START-HERE.html`: it redirected to the offline dashboard, rendered 25 cards and the `0 of 25` progress dashboard, followed the first lesson link, and loaded its two reference images with no broken images. On the offline lesson, a parts checkbox and build check persisted after reload; Reset progress cleared both and returned progress to `0 of 5`.
- Chromium browser QA also opened the LAN-served `http://192.168.50.24:8080/web/index.html`: it rendered 25 cards, the progress dashboard, and both static-data/app scripts.
- A separate headless Chromium run with browser logging enabled completed the offline launch without JavaScript console errors; Chromium emitted only host-environment warnings about sandbox, D-Bus screensaver, and persistent-store shutdown tasks.

## Limitations

- Browser validation used local Chromium on this machine; it does not prove behavior in every browser or operating system.
- No physical Arduino hardware was assembled or tested.
- The package intentionally excludes source packs, tests, reviews, Git metadata, and development tooling.
