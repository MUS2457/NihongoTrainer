# NihongoTrainer

NihongoTrainer is a modular Japanese learning application designed to help study vocabulary, kanji, and grammar efficiently. The project uses clean backend architecture with clear separation between logic and data storage.

## Project Structure

```
NIHONGOTRAINER/
│
├── CORE/
│   ├── quiz.py              # Quiz generation and evaluation logic
│   ├── word_manager.py      # Handles word addition, deletion, and lookup
│   ├── word_module.py       # Core word data structures and utilities
│
├── STORAGE/
│   ├── storage.py           # File I/O and persistent data management
│
├── vocab.json               # Vocabulary database
├── main.py                  # Entry point for running the app
├── venv/                    # Virtual environment
└── README.md                # Project documentation
```

## Features

- Vocabulary management (add, edit, delete, search)
- Quiz generation from stored words
- Persistent JSON storage
- Modular architecture for easy expansion
- Clean separation between logic and storage layers

## How to Run

1. Activate the virtual environment:
2. Run the main program:


## Requirements

- Python 3.10+
- Virtual environment (venv)
- JSON data file (vocab.json)

## Goals

- Support Japanese language learning for school starting July 2026
- Demonstrate backend engineering mastery through modular design
- Expand into a full-featured language trainer with quizzes and analytics

## Future Improvements

- Add spaced repetition system (SRS)
- Integrate kana/kanji practice modules
- Add progress tracking and statistics
- Build a simple CLI or GUI interface
- Migrate storage from JSON to SQLite
