from CORE.word_module import Kotoba
from STORAGE.storage import save_db, load_db

class KotobaManager() :

    def __init__(self) :
        self.db = load_db()

    def save(self) :
        save_db(self.db)  # save data in the memory

    def list(self) :
        if not self.db :
            print("No words has been founded, yet.")
            return
        
        for i, w in enumerate(self.db, start= 1) :
            print(f"{i}. {w['word']} ({w['romaji']}) - {w['meaning']}")

    def add_kotoba(self):
        print("\n=== Add New Word ===")

        while True :
            word = input("Kana: ").strip()
            if not word or any(char.isdigit() for char in word) or any(char.isalpha() for char in word) :
                print("Enter a word with japanese characters only")
                continue

            romaji = input("Romaji: ").strip()
            if not romaji or any(char.isdigit() for char in romaji) :
                print("invalid input")
                continue

            meaning = input("Meaning: ").strip()
            if not meaning or any(char.isdigit() for char in meaning) :
                print("invalid input")
                continue

            example = input("Example (optional): ").strip()

            kotoba = Kotoba(word, romaji, meaning,example)

            self.db.append(kotoba.to_dict())

            self.save()

            print("Word has been added")

    def delete_word(self) :
        print("delete word")
        self.list()
        
        while True :
            choice = input("Enter the number of the word you want to delete").strip()

            if not choice.isdigit() :
                ("Enter a number")
                continue

            index = int(choice) - 1

            if index < 0 or index >= len(self.db) :
                print("Invalid number")
                continue
            
            selected = self.db[index]

            confirm = input(f"Are you sure you want to remove : {selected['word']}=={selected['romaji']} (y/n)").strip().lower()

            if confirm == "y" :

                self.db.pop(index)
                self.save()
                print(f"the word '{selected['word']}={selected['romaji']}'")
                return #removed = self.db.pop(index)  # its a list ,so used pop to remove item based index it was my first version

            print("Deletion cancelled. Returning to main menu.")
            return

            

            




