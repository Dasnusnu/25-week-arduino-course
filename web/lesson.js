const lessonKey = `25week-guide:${window.location.pathname}:checks`;
const partsKey = `25week-guide:${window.location.pathname}:parts`;
const boxes = [...document.querySelectorAll('[data-step]')];
const progress = document.querySelector('#progress');
const progressText = document.querySelector('#progress-text');

function readSaved(key) {
  try {
    return new Set(JSON.parse(localStorage.getItem(key) || '[]'));
  } catch {
    return new Set();
  }
}

const savedChecks = readSaved(lessonKey);
const savedParts = readSaved(partsKey);
const partBoxes = [...document.querySelectorAll('.parts li')].map((item, index) => {
  const text = item.textContent.trim();
  const input = document.createElement('input');
  const id = `part-checkbox-${index + 1}`;
  input.type = 'checkbox';
  input.id = id;
  input.dataset.part = String(index + 1);
  input.checked = savedParts.has(input.dataset.part);

  const label = document.createElement('label');
  label.className = 'part-check';
  label.htmlFor = id;
  label.append(input, document.createTextNode(` ${text}`));
  item.replaceChildren(label);
  return input;
});

function updateProgress() {
  const complete = boxes.filter((box) => box.checked).length;
  progress.value = complete;
  progressText.textContent = `${complete} of ${boxes.length} checks complete.`;
  localStorage.setItem(lessonKey, JSON.stringify(boxes.filter((box) => box.checked).map((box) => box.dataset.step)));
}

function updateParts() {
  localStorage.setItem(partsKey, JSON.stringify(partBoxes.filter((box) => box.checked).map((box) => box.dataset.part)));
}

boxes.forEach((box) => {
  box.checked = savedChecks.has(box.dataset.step);
  box.addEventListener('change', updateProgress);
});
partBoxes.forEach((box) => box.addEventListener('change', updateParts));
document.querySelector('#reset-progress').addEventListener('click', () => {
  boxes.forEach((box) => { box.checked = false; });
  partBoxes.forEach((box) => { box.checked = false; });
  updateProgress();
  updateParts();
});
updateProgress();