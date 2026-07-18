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
        
        words = self.get_due_words()
        remaining = len(words)

        if not words :
            print("No words are due for review.")
            return
        
        print(f"You have {len(words)} words due for review:")

        stats = {"Completely": 0,
                 "Partially": 0,
                 "Not at all": 0
        }


        for w in words :
            print(f"Remaining words : {remaining}")
            remaining -= 1

            print(f"{w['word']} ({w['romaji']}) - {w['meaning']}")
            if w.get("example") :
                print(f"Example: {w['example']}")
            
            input("Press Enter to continue to the next word...")

            familiarity = list(("Completely", "Partially", "Not at all"))
        
            
            while True :
                print("==Familiarity scale==")

                for i, l in enumerate(familiarity, start = 1) :
                    print(f"{i}. {l}")

                remember = input("Enter a number from (1 to 3) based on familiarity scale , or 'q' to quit").strip()

                if remember.lower() == "q" :
                    print("Returning to main menu")
                    self.save()
                    return

                if not remember.isdigit() or int(remember) not  in [1,2,3] :
                    print("Invalid choice")
                    continue

                index = int(remember) -1 

                stats[familiarity[index]] += 1

                if familiarity[index] == "Completely" :
                    w["level"] += 1

                elif familiarity[index] == "Partially" :
                    w["level"] = max(0, w["level"] - 1)

                else :
                    w["level"] = 0
            
                w["next_review"] = self.calculate_next_review(w["level"])

        print(f" Words reviewed : {len(words)}")

        print(f" completed : {stats['Completely']}")

        if int(stats["Completely"]) == len(words) :
            print("すごい記憶力ですね。流暢さを追求する道を進み続けてください。短いですから！！")
        
        print(f" partially : {stats['Partially']}")

        if int(stats["Partially"]) >= (0.5 * len(words)):
            print(f"流暢になるまでの道のりは長いので、もっと勉強しましょう（怠惰ではありません")

        print(f"Not at all : {stats['Not at all']}")

        if int(stats["Not at all"]) >= (0.6 * len(words)) :
            print(f"ロックインしないと、流暢さは（人生において）達成できなくなります")

        self.save()
        print("Words have been reviewed.")
        return
    
    def get_due_words(self) :
        today = datetime.now()
        due_words = [w for w in self.db if w["next_review"] is None or datetime.strptime(w["next_review"], "%Y-%m-%d") <= today]

        return due_words
    

    def calculate_next_review(self, index) :
        intervals = [0, 1, 2, 4, 7, 14, 30, 60, 120]
        Days = intervals[index] if index < len(intervals) else intervals[-1] # < means included 

        return (datetime.now() + timedelta(days=Days)).strftime("%Y-%m-%d")
