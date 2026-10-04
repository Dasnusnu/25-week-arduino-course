from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "web"


class CurriculumProgressContractTest(unittest.TestCase):
    def test_all_lesson_pages_keep_parts_and_five_build_checks(self):
        pages = sorted((WEB / "lessons").glob("*.html"))
        self.assertEqual(len(pages), 25)
        for page in pages:
            content = page.read_text(encoding="utf-8")
            self.assertIn('class="parts"', content, page.name)
            self.assertEqual(len(re.findall(r'data-step="[^"]+"', content)), 5, page.name)

    def test_lesson_script_keeps_build_and_parts_state_separate(self):
        script = (WEB / "lesson.js").read_text(encoding="utf-8")
        self.assertIn('const lessonKey = `25week-guide:${window.location.pathname}:checks`;', script)
        self.assertIn('const partsKey = `25week-guide:${window.location.pathname}:parts`;', script)
        self.assertIn("document.querySelectorAll('.parts li')", script)
        self.assertIn('part-checkbox-', script)
        self.assertIn('partsKey', script)
        self.assertIn('reset-progress', script)

    def test_lesson_css_stacks_accessible_part_rows(self):
        css = (WEB / "lesson.css").read_text(encoding="utf-8")
        self.assertRegex(css, r'\.parts\{[^}]*grid-template-columns:1fr')
        self.assertIn('.part-check', css)
        self.assertIn('.part-check input', css)

    def test_dashboard_contract_shows_lesson_and_curriculum_progress(self):
        page = (WEB / "index.html").read_text(encoding="utf-8")
        script = (WEB / "app.js").read_text(encoding="utf-8")
        css = (WEB / "styles.css").read_text(encoding="utf-8")
        self.assertIn('id="curriculum-progress-text"', page)
        self.assertIn('id="curriculum-progress"', page)
        self.assertIn('class="lesson-progress-text"', page)
        self.assertIn('class="lesson-progress"', page)
        self.assertIn('new URL(`lessons/${filename}`, window.location.href).pathname', script)
        self.assertIn('const BUILD_CHECKS_PER_LESSON = 5;', script)
        self.assertIn('curriculum-progress', script)
        self.assertIn('lesson--complete', script)
        self.assertIn('.lesson-progress', css)
        self.assertIn('.lesson--complete', css)


if __name__ == "__main__":
    unittest.main()
