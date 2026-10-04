from pathlib import Path
import json
import re
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "web"
ZIP_PATH = ROOT / "dist" / "25-week-arduino-guide-offline.zip"


class OfflineDistributionContractTest(unittest.TestCase):
    def test_static_lesson_data_matches_inventory(self):
        inventory = json.loads((ROOT / "data" / "lessons.json").read_text(encoding="utf-8"))
        script = (WEB / "lessons-data.js").read_text(encoding="utf-8")
        match = re.search(r"window\.LESSONS_DATA\s*=\s*(\[.*\]);\s*$", script, re.DOTALL)
        if match is None:
            self.fail("lessons-data.js must assign window.LESSONS_DATA")
        self.assertEqual(json.loads(match.group(1)), inventory)

    def test_dashboard_uses_static_data_before_app_without_fetch(self):
        page = (WEB / "index.html").read_text(encoding="utf-8")
        script = (WEB / "app.js").read_text(encoding="utf-8")
        self.assertLess(page.index('src="lessons-data.js"'), page.index('src="app.js"'))
        self.assertNotIn("fetch(", script)
        self.assertIn("window.LESSONS_DATA", script)
        self.assertIn("Curriculum load error", script)

    def test_offline_start_and_quickstart_explain_file_launch(self):
        start = (ROOT / "START-HERE.html").read_text(encoding="utf-8")
        quickstart = (ROOT / "OFFLINE-QUICKSTART.md").read_text(encoding="utf-8")
        self.assertIn('web/index.html', start)
        self.assertIn('localStorage', quickstart)
        self.assertIn('modern browser', quickstart.lower())

    def test_package_contains_only_portable_user_files(self):
        self.assertTrue(ZIP_PATH.is_file())
        with zipfile.ZipFile(ZIP_PATH) as package:
            names = package.namelist()
        self.assertIn("START-HERE.html", names)
        self.assertIn("OFFLINE-QUICKSTART.md", names)
        self.assertIn("web/index.html", names)
        self.assertIn("web/lessons-data.js", names)
        self.assertEqual(len([name for name in names if name.startswith("web/lessons/") and name.endswith(".html")]), 25)
        forbidden_prefixes = ("sources/", ".git/", "tests/", "reviews/", ".hermes/", "data/", "dist/", "tools/")
        self.assertFalse([name for name in names if name.startswith(forbidden_prefixes)], names)


if __name__ == "__main__":
    unittest.main()
