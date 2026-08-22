# NihongoTrainer

NihongoTrainer is a modular Japanese learning application designed to help me study vocabulary, kanji, and grammar efficiently. The project uses clean backend architecture with clear separation between logic and data storage.

## Project Structure

```
NIHONGOTRAINER/
│
├── CORE/
│   ├── color_module.py      # ANSI color utilities for CLI feedback
│   ├── kana_module.py       # Kana data model and utilities
│   ├── word_module.py       # Word data model and core logic
│
├── QUIZ/
│   ├── kana_quiz.py         # Hiragana/Katakana quiz logic with color feedback
│   ├── word_manager.py      # Word management (add, delete, update, search)
│   ├── word_quiz.py         # Word quiz modes (romaji, kana, meaning)
│
├── STORAGE/
│   ├── kana_storage.py      # Kana data loading and persistence
│   ├── storage.py           # General JSON and file I/O
│
├── DB/
│   ├── kana.csv             # Hiragana and kata dataset
│   ├── words.json           # Vocabulary database (word → meaning → kana)
│
├── main.py                  # Entry point for running the CLI app
└── README.md                # Project documentation
```

---

## 🚀 Features

- Vocabulary management (add, edit, delete, search)
- Kana quizzes (hiragana, katakana)
- Word quizzes (romaji, kana, meaning)
- Color feedback for correct/incorrect answers
- Persistent JSON + CSV storage
- Modular architecture for easy expansion
- Clean separation between logic, storage, and data layers

---

## 🧠 How to Run

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate



## Requirements

- Python 3.10+
- Virtual environment (venv)
- JSON data file (vocab.json)

## Goals

- Support Japanese language learning for school starting 
- Demonstrate backend engineering mastery through modular design
- Expand into a full-featured language trainer with quizzes and analytics

## Future Improvements

- Migrate storage from JSON to SQLite
