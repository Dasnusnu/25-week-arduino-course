const state = { lessons: [], term: '', onlyCovered: false };
const grid = document.querySelector('#lessons');
const count = document.querySelector('#count');
const template = document.querySelector('#lesson-template');
const curriculumProgress = document.querySelector('#curriculum-progress');
const curriculumProgressText = document.querySelector('#curriculum-progress-text');
const BUILD_CHECKS_PER_LESSON = 5;
const lessonPages = {
  1: '01-light-your-first-led.html', 2: '02-make-some-noise.html', 3: '03-the-melody-machine.html',
  4: '04-the-control-knob.html', 5: '05-the-darkness-detector.html', 6: '06-mix-your-own-colours.html',
  7: '07-make-numbers-appear.html', 8: '08-the-counting-machine.html', 9: '09-the-room-thermometer.html',
  10: '10-the-water-detector.html', 11: '11-words-on-a-real-screen.html', 12: '12-the-secret-password-pad.html',
  13: '13-the-game-style-joystick.html', 14: '14-the-clap-trigger.html', 15: '15-more-lights-than-pins.html',
  16: '16-small-board-big-switch.html', 17: '17-the-precision-spinner.html', 18: '18-point-it-anywhere.html',
  19: '19-a-clock-that-never-forgets.html', 20: '20-control-it-by-remote.html', 21: '21-the-remote-controlled-lamp.html',
  22: '22-the-card-scanner.html', 23: '23-green-light-red-light.html', 24: '24-the-access-system.html',
  25: '25-the-rfid-door-lock.html',
};

function lessonStorageKey(filename) {
  const pathname = new URL(`lessons/${filename}`, window.location.href).pathname;
  return `25week-guide:${pathname}:checks`;
}

function checkedSteps(filename) {
  try {
    const saved = JSON.parse(localStorage.getItem(lessonStorageKey(filename)) || '[]');
    return Array.isArray(saved)
      ? new Set(saved.filter((step) => ['1', '2', '3', '4', '5'].includes(String(step)))).size
      : 0;
  } catch {
    return 0;
  }
}

function updateCurriculumProgress() {
  const counts = state.lessons.map((lesson) => checkedSteps(lessonPages[lesson.week]));
  const completedLessons = counts.filter((complete) => complete === BUILD_CHECKS_PER_LESSON).length;
  const totalChecks = counts.reduce((sum, complete) => sum + complete, 0);
  curriculumProgress.value = completedLessons;
  curriculumProgress.setAttribute('aria-label', `${completedLessons} of ${state.lessons.length} lessons complete`);
  curriculumProgressText.textContent = `${completedLessons} of ${state.lessons.length} lessons complete · ${totalChecks} of ${state.lessons.length * BUILD_CHECKS_PER_LESSON} build checks complete.`;
}

function render() {
  const term = state.term.toLowerCase().trim();
  const visible = state.lessons.filter((lesson) => {
    const haystack = [lesson.title, lesson.summary, ...lesson.concepts, lesson.source].join(' ').toLowerCase();
    return (!term || haystack.includes(term)) && (!state.onlyCovered || lesson.covered);
  });
  grid.replaceChildren();
  count.textContent = `${visible.length} of ${state.lessons.length} lessons`;
  updateCurriculumProgress();
  if (!visible.length) {
    const empty = document.createElement('p'); empty.className = 'empty'; empty.textContent = 'No lessons match that filter.'; grid.append(empty); return;
  }
  for (const lesson of visible) {
    const node = template.content.cloneNode(true);
    const filename = lessonPages[lesson.week];
    const complete = checkedSteps(filename);
    node.querySelector('.week').textContent = `W${String(lesson.week).padStart(2, '0')}`;
    node.querySelector('.status').textContent = lesson.covered ? 'source pack present' : 'source gap';
    node.querySelector('h2').textContent = lesson.title;
    node.querySelector('.summary').textContent = lesson.summary;
    node.querySelector('.concepts').textContent = `Skills: ${lesson.concepts.join(' · ')}`;
    node.querySelector('.coverage').textContent = `Reference: ${lesson.source}`;
    const progressText = node.querySelector('.lesson-progress-text');
    const progress = node.querySelector('.lesson-progress');
    progress.value = complete;
    progress.setAttribute('aria-label', `${complete} of ${BUILD_CHECKS_PER_LESSON} build checks complete`);
    progressText.textContent = `${complete} of ${BUILD_CHECKS_PER_LESSON} build checks`;
    node.querySelector('.lesson').classList.toggle('lesson--complete', complete === BUILD_CHECKS_PER_LESSON);
    const link = node.querySelector('.open-lesson');
    link.href = `lessons/${filename}`;
    link.hidden = false;
    grid.append(node);
  }
}

document.querySelector('#search').addEventListener('input', (event) => { state.term = event.target.value; render(); });
document.querySelector('#covered').addEventListener('change', (event) => { state.onlyCovered = event.target.checked; render(); });
window.addEventListener('storage', (event) => {
  if (event.key?.startsWith('25week-guide:') && event.key.endsWith(':checks')) render();
});
fetch('../data/lessons.json').then((response) => {
  if (!response.ok) throw new Error(`Could not load curriculum (${response.status})`);
  return response.json();
}).then((lessons) => { state.lessons = lessons; render(); }).catch((error) => {
  grid.textContent = `Curriculum load error: ${error.message}`;
  console.error(error);
});