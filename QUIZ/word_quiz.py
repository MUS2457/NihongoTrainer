import random
from STORAGE.storage import load_db, save_db
from collections import defaultdict
from CORE import word_module, color_module

class KotobaQuizzer :
    def __init__(self) :
        data = load_db()
        self.db = [word_module.Kotoba.from_dict(i) for i in data]
    
    def save(self) :
        save_db(self.db)

    
    def guessing(self, asked, responced) :
        interval = min(len(self.db), 15)
        seen = set()
        score = 0
        fails = 0
        duplicates = defaultdict(int)
        shown = 0
        failed_counter = defaultdict(int)
        color = color_module.Color()


        while score < interval :
            w = random.choice(self.db)
            shown += 1

            user = input(f"Enter the {responced.capitalize()} corresponding to this {getattr(w,asked)} ").strip()

            if user.lower() == getattr(w,responced) :
                if w.word in seen :
                    print(color.GREEN + "Correct, Already counted!" + color.RESET)

                    duplicates[w.word] += 1

                else :
                    print(color.GREEN + "Correct!" + color.RESET)
                    seen.add(w.word)
                    score += 1

            else :
                duplicates[w.word] += 1
                failed_counter[w.word] += 1

                fails += 1

                print(color.RED + "Your answer is incorrect" + color.RESET)
                print(f"word : {w.word}")
                print(f"romaji : {w.romaji}")
                print(f"Meaning : {w.meaning}")
                print(f"Example : {w.example or 'No example provided'}")

        unique_attempts = False

        if duplicates :
            tl_duplicates , most_shown = self.duplicate_manager(duplicates)
            unique_attempts = shown - tl_duplicates

        
        if unique_attempts is False :
            fail_rate = (fails / shown) * 100

        else :
            fail_rate = (fails / unique_attempts) * 100 


        succes_rate = 100 - fail_rate 
        
        print(f"Succes rate : {succes_rate: .2f}")
        
        if failed_counter :
            failed_max, results = self.failed_word_filter(failed_counter)
            
            print(f"Your fails rate : {fail_rate: .2f}")
            print("Your most failed word\n")
            print(f"Word : {failed_max.word}")
            print(f"romaji : {failed_max.romaji}")
            print(f"Meaning : {failed_max.meaning}")
            print(f"Example : {failed_max.example or 'No example provided'}")

            others = [w for w in results if w != failed_max]

            if others :
                print("Other failed words")
                for d in others :
                    print()
                    print(f"Word : {d.word}")
                    print(f"romaji : {d.romaji}")
                    print(f"Meaning : {d.meaning}")
                    print(f"Example : {d.example or 'No example provided'}")

        if duplicates :
            print()
            print(f"Most shown word : {most_shown.word}")
            print(f"romaji : {most_shown.romaji}")
            print(f"Meaning : {most_shown.meaning}")
            print(f"Example : {most_shown.example or 'No example provided'}")
        



    def failed_word_filter(self, dict) :
            failed_word = max(dict, key = dict.get)
            max_failed = next(d for d in self.db if d.word == failed_word)
            results = [w for w in self.db if w.word in dict]
            return max_failed, results


    def duplicate_manager(self, duplicates) :
        real_duplicates = [i for i,f in duplicates.items() if f > 1]
        tl_duplicates = sum(duplicates[i] for i in real_duplicates) - len(real_duplicates)
        most_shown = next(w for w in self.db if w.word == max(duplicates, key = duplicates.get))

        return tl_duplicates, most_shown

    def quizzer_romanji(self) :
        self.guessing("word", "romaji")

    def quizzer_kana(self) :
        self.guessing("romaji", "word")

    def quizzer_meaning(self) :
        self.guessing("word", "meaning")
        
          
        