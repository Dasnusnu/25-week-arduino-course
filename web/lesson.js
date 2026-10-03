const lessonKey = '25week-guide:lesson-01:checks';
const boxes = [...document.querySelectorAll('[data-step]')];
const progress = document.querySelector('#progress');
const progressText = document.querySelector('#progress-text');
const saved = new Set(JSON.parse(localStorage.getItem(lessonKey) || '[]'));

function updateProgress() {
  const complete = boxes.filter((box) => box.checked).length;
  progress.value = complete;
  progressText.textContent = `${complete} of ${boxes.length} checks complete.`;
  localStorage.setItem(lessonKey, JSON.stringify(boxes.filter((box) => box.checked).map((box) => box.dataset.step)));
}

boxes.forEach((box) => {
  box.checked = saved.has(box.dataset.step);
  box.addEventListener('change', updateProgress);
});
document.querySelector('#reset-progress').addEventListener('click', () => {
  boxes.forEach((box) => { box.checked = false; });
  updateProgress();
});
updateProgress();
