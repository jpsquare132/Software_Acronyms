# Software Acronym Manager
This Python application is a simple command-line tool designed to store and retrieve software development acronyms. It acts as a digital dictionary, allowing users to manage a growing list of technical terminology through a text-based database.

## Core Functionality

The program offers two primary features managed through a central menu:

Search and Lookup: The tool scans a local text file (input.txt) for a specific acronym. It is designed to be case-insensitive, ensuring that searches for "api" or "API" both return the correct definition. If the acronym exists, the program displays the full entry; if not, it alerts the user.

Data Entry: Users can expand the database by adding new acronyms and their definitions directly through the interface. The program appends this information to the existing file, ensuring no previous data is lost.

## Technical Workflow

The code utilizes basic file I/O operations, opening the text file in "read" mode for lookups and "append" mode for new entries. It includes error handling to prevent crashes if the database file is missing and uses a simple loop-based menu to guide the user through their choices.
