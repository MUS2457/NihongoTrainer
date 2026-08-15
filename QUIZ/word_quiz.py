import random
from STORAGE.storage import load_db, save_db
from collections import defaultdict
from CORE import word_module

class KotobaQuizzer :
    def __init__(self) :
        data = load_db()
        self.db = [word_module.Kotoba.from_dict(i) for i in data]
    
    def save(self) :
        save_db(self.db)

    
    def guessing(self) :
        interval = min(len(self.db), 15)
        seen = set()
        score = 0
        fails = 0
        duplicates = defaultdict(int)
        shown = 0
        failed_counter = defaultdict(int)

        while score < 3 :
            w = random.choice(self.db)
            shown += 1

            user = input(f"Enter the 'Romaji' corresponding to this {w.word} ").strip()

            if user.lower() == w.romaji :
                if w.word in seen :
                    duplicates[w.word] += 1

                else :
                    seen.add(w.word)
                    score += 1

            else :
                duplicates[w.word] += 1
                failed_counter[w.word] += 1

                fails += 1

                print("Your answer is incorrect")
                print(f"word : {w.word}")
                print(f"romaji : {w.romaji}")
                print(f"Meaning : {w.meaning}")
                print(f"Example : {w.example or 'No example provided'}")

        if failed_counter :
            max_failde , results = self.failed_word_filter(duplicates)
            print(max_failde)
            for i in results :
                 print(i)



    def failed_word_filter(self, dict) :
            failed_word = max(dict, key = dict.get)
            max_failed = next(d for d in self.db if d.word == failed_word)
            results = [w for w in self.db if w.word in dict]
            return max_failed, results
        
        
          
        