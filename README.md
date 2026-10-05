# 25-Week Arduino Guide

A complete set of interactive Arduino lessons for a guided beginner. The guide opens in a regular web browser and remembers each learner's parts checks and build progress on the device they are using.

## The easiest way to use the guide

Download the offline ZIP from the [latest GitHub release](https://github.com/Dasnusnu/25-week-arduino-course/releases/latest), then:

1. Extract the ZIP somewhere easy to find, such as Downloads or the Desktop.
2. Open the extracted folder.
3. Double-click **START-HERE.html**.
4. If your computer asks which app to use, choose a modern browser such as Chrome, Edge, Firefox, or Safari.

That is all. There is nothing to install and no account, terminal, Python, Node, or web server is needed.

Your lesson progress and parts checklists stay in the browser on that computer. They do not automatically move to another computer or browser. Each lesson has a **Reset progress** button if you want to start that lesson again.

## Other ways to run it

### Open an already extracted copy

If someone has already given you the extracted guide folder, you do not need to download it again. Open that folder and double-click **START-HERE.html**.

### Use the shared LAN copy

If someone running the guide has given you a local web address, open that address in a browser on the same network. The guide behaves the same way as the offline copy, including saved progress in your browser.

### Run a local preview for editing or testing

This option is for someone comfortable with a terminal. From the project folder, run:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080/web/` in a browser. Stop the preview by returning to the terminal and pressing `Ctrl+C`.

## What is included

- 25 step-by-step interactive lessons
- Required-parts checklists
- Five build checks per lesson
- A main dashboard showing lesson and curriculum progress
- Picture references and direct reference pages for each lesson
- An offline package that works without a server

## A note about progress

The guide uses your browser's local storage to remember checkmarks. Clearing browser site data, using private/incognito mode, switching browsers, or moving to another computer can remove or separate that saved progress. The lesson content itself is not changed by your checkmarks.

## For maintainers

The browser dashboard uses `web/lessons-data.js`, a static browser copy of the lesson inventory. If the lesson inventory changes, rebuild the offline ZIP with:

```bash
python3 tools/build_offline_package.py
```

The project is a noncommercial educational guide. Third-party reference images and technical facts are attributed in the individual lessons and source inventory. Do not remove attribution or use third-party material commercially without confirming the relevant rights.
