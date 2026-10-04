#!/usr/bin/env python3
"""Generate browser-local curriculum data and the portable offline ZIP."""
from __future__ import annotations

import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "dist" / "25-week-arduino-guide-offline.zip"
INVENTORY = ROOT / "data" / "lessons.json"
STATIC_DATA = ROOT / "web" / "lessons-data.js"
INCLUDE = ("START-HERE.html", "OFFLINE-QUICKSTART.md", "web")


def generate_static_data() -> None:
    lessons = json.loads(INVENTORY.read_text(encoding="utf-8"))
    payload = json.dumps(lessons, ensure_ascii=False, indent=2)
    STATIC_DATA.write_text(
        "// Generated from data/lessons.json by tools/build_offline_package.py.\n"
        "// Do not edit by hand; rerun this script after inventory changes.\n"
        f"window.LESSONS_DATA = {payload};\n",
        encoding="utf-8",
    )


def add_path(package: zipfile.ZipFile, path: Path) -> None:
    if path.is_file():
        package.write(path, path.relative_to(ROOT).as_posix())
        return
    for child in sorted(path.rglob("*")):
        if child.is_file():
            package.write(child, child.relative_to(ROOT).as_posix())


def build_package() -> None:
    PACKAGE.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(PACKAGE, "w", zipfile.ZIP_DEFLATED) as package:
        for item in INCLUDE:
            add_path(package, ROOT / item)


if __name__ == "__main__":
    generate_static_data()
    build_package()
    print(PACKAGE)
