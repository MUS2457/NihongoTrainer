import json
import os


ROOT = os.path.dirname(os.path.dirname(__file__))  # go up from STORAGE , __file__ represent current position, so we back 2 times
DB_DIR = os.path.join(ROOT, "DB")  # dirname == back one step path name ex :ftp/db/.py after become ftp/db
file_path = os.path.join(DB_DIR, "vocab.json")  # the file itself


def load_db():
    if not os.path.isfile(file_path) :
        print("Add Words first ")
        return []

    try :
        with open(file_path, "r", encoding="utf-8") as kotoba:
            return json.load(kotoba)

    except Exception as e :
        print("Error loading data",e)
        return []


def save_db(data):
    with open(file_path, "w", encoding="utf-8") as kotoba:
        json.dump(data, kotoba, ensure_ascii=False, indent=4)
