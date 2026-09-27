# Terminal Calendar & Event Manager

## Overview
A lightweight, completely text-based terminal calendar application written in Python. It allows users to view monthly calendars and manage personal notes or events directly from the command line without needing a graphical interface.

## Features
* Interactive command-line menu.
* Generate and view full monthly text calendars.
* Add custom events or notes attached to specific dates.
* View a complete log of all saved events.
* Offline data persistence using standard text files.

## Technologies/Tools Used
* Python 3.x
* Python Standard Libraries (`calendar`)
* Local `.txt` file storage

## Steps to Install & Run
1. Ensure Python 3 is installed on your machine.
2. Clone this repository to your local computer.
3. Open a terminal or command prompt inside the project folder.
4. Run the command: `python main.py`

## Instructions for Testing
1. Run the application using the command above.
2. Select option `1` to view a calendar (enter a year and month).
3. Select option `2` to add an event. Enter a test date (e.g., "10-Nov") and a test note.
4. Select option `3` to verify your note is displayed.
5. Select option `4` to exit the application.
6. Run the application again and select option `3`. Your note will still be there, proving the local storage works.

## Screenshots
*(Since this is a purely terminal-based application, interactions occur via standard text input/output in the command prompt. No graphical GUI screenshots are applicable.)*