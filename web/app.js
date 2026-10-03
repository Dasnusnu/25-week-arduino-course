const state = { lessons: [], term: '', onlyCovered: false };
const grid = document.querySelector('#lessons');
const count = document.querySelector('#count');
const template = document.querySelector('#lesson-template');

function render() {
  const term = state.term.toLowerCase().trim();
  const visible = state.lessons.filter((lesson) => {
    const haystack = [lesson.title, lesson.summary, ...lesson.concepts, lesson.source].join(' ').toLowerCase();
    return (!term || haystack.includes(term)) && (!state.onlyCovered || lesson.covered);
  });
  grid.replaceChildren();
  count.textContent = `${visible.length} of ${state.lessons.length} lessons`;
  if (!visible.length) {
    const empty = document.createElement('p'); empty.className = 'empty'; empty.textContent = 'No lessons match that filter.'; grid.append(empty); return;
  }
  for (const lesson of visible) {
    const node = template.content.cloneNode(true);
    node.querySelector('.week').textContent = `W${String(lesson.week).padStart(2, '0')}`;
    node.querySelector('.status').textContent = lesson.covered ? 'source pack present' : 'source gap';
    node.querySelector('h2').textContent = lesson.title;
    node.querySelector('.summary').textContent = lesson.summary;
    node.querySelector('.concepts').textContent = `Skills: ${lesson.concepts.join(' · ')}`;
    node.querySelector('.coverage').textContent = `Reference: ${lesson.source}`;
    const lessonPages = {
      1: '01-light-your-first-led.html',
      2: '02-make-some-noise.html',
      3: '03-the-melody-machine.html',
      4: '04-the-control-knob.html',
      5: '05-the-darkness-detector.html',
      6: '06-mix-your-own-colours.html',
      7: '07-make-numbers-appear.html',
      8: '08-the-counting-machine.html',
      9: '09-the-room-thermometer.html',
      10: '10-the-water-detector.html',
      11: '11-words-on-a-real-screen.html',
      12: '12-the-secret-password-pad.html',
      13: '13-the-game-style-joystick.html',
      14: '14-the-clap-trigger.html',
      15: '15-more-lights-than-pins.html',
    };
    if (lessonPages[lesson.week]) {
      const link = node.querySelector('.open-lesson');
      link.href = `lessons/${lessonPages[lesson.week]}`;
      link.hidden = false;
    }
    grid.append(node);
  }
}

document.querySelector('#search').addEventListener('input', (event) => { state.term = event.target.value; render(); });
document.querySelector('#covered').addEventListener('change', (event) => { state.onlyCovered = event.target.checked; render(); });
fetch('../data/lessons.json').then((response) => {
  if (!response.ok) throw new Error(`Could not load curriculum (${response.status})`);
  return response.json();
}).then((lessons) => { state.lessons = lessons; render(); }).catch((error) => {
  grid.textContent = `Curriculum load error: ${error.message}`;
  console.error(error);
});
