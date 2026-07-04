import json
import os

FILE_NAME = "vocab.json"

def load_db():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r", encoding="utf-8") as kotoba:
        return json.load(kotoba)


def save_db(data):
    with open(FILE_NAME, "w", encoding="utf-8") as kotoba:
        json.dump(data, kotoba, ensure_ascii=False, indent=4)
