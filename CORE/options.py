from CORE.word_module import Kotoba
from STORAGE.storage import save_db, load_db
from datetime import datetime, timedelta

class KotobaManager() :

    def __init__(self) :
        self.db = load_db()

    def save(self) :
        save_db(self.db)  # (self.db) representthe data in the memory (loaded and modiefied in later on)

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

    def delete_kotoba(self) :
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

            

    def Update_kotoba(self) :
        print("==Update word==")
        self.list()

        while True :
            choice = input("Enter the number of the word you want to update!").strip()

            if not choice.isdigit() :
                print("enter a valid number")
                continue

            index = int(choice) - 1 

            if index < 0 or index >= len (self.db) :
                print("the number selected doesnt match any result")
                continue

            selected = self.db[index]

            new_word = input(f"New Kana [{selected['word']}]: ").strip()
            new_romaji = input(f"New Romaji [{selected['romaji']}]: ").strip()
            new_meaning = input(f"New Meaning [{selected['meaning']}]: ").strip()
            new_example = input(f"New Example [{selected.get('example', '')}]: ").strip()

            if new_word :
                selected["word"] = new_word
            
            if new_romaji :
                selected["romaji"] = new_romaji

            if new_meaning :
                selected["meaning"] = new_meaning

            selected["example"] = new_example

            self.save()
            print("✔ Word updated successfully.")
            return
    
    def search_kotoba(self) :
        print("==Search word==")

        search_term = input("Enter the word you want to search for (word,romaji, meaning or example): ").strip().lower()
        
        results = []

        for w in self.db :
            
            word = w["word"]
            romaji = w["romaji"].lower()
            meaning = w["meaning"].lower()
            example = w.get("example", "").lower()
        

            if (search_term in word or
                search_term in romaji or
                search_term in meaning or
                search_term in example) :
                results.append(w)
        
        if not results :
            print("No matching words found.")
            return
        
        print(f"Found {len(results)} matching words:")
        for i, w in enumerate(results, start=1) :
            print(f"{i}. {w['word']} ({w['romaji']}) - {w['meaning']} - Example: {w.get('example', 'no example provided')}")
            
        return results
    
    def review_kotoba(self) :
        print("==Review words==")
        if not self.db :
            print("No words available for review.")
            return
        
        today = datetime.now()

        for w in self.db :
            if w["next_review"] is None :
                due = True
            
            else :
                next_date = datetime.strptime(w["next_review"], "%Y-%m-%d")
                due = next_date <= today
 

            if due :
                print(f"Review word: {w['word']} ({w['romaji']}) - {w['meaning']}")

                input("Press Enter to continue to the next word...")

                w["level"] += 1
                Days = w["level"] * 2
                w["next_review"] = (today + timedelta(days=Days)).strftime("%Y-%m-%d")

        self.save()
        print("Words have been reviewed.")