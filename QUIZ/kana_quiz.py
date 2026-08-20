from STORAGE import kana_storage
from CORE import kana_module, color_module
import random
import collections


class KanaManager() :

    def __init__(self) :
        raw = kana_storage.load_kana()
        self.all = [kana_module.Kana.from_dict(d) for d in raw]
        self.hiragana = [h for h in self.all if h.type in ("hiragana", "hiragana-small")]
        self.katakana = [k for k in self.all if k.type in  ("katakana", "katakana-small")]
        
    

    def quizzer (self, quetion) :
        score = 0
        shown = 0
        failed = 0
        duplicates = collections.defaultdict(int)
        seen = set()
        color = color_module.Color()

        while score < 20 :
            char = random.choice(getattr(self,quetion))
            shown += 1

            user = input(f"Enter the 'Romaji' corresponding to this {char.kana} ").strip()

            if user.lower() == char.romaji :

                if char.kana in seen :
                    print(color.GREEN + "Correct, Already counted!" + color.RESET)
                    duplicates[char.kana] += 1

                else :
                    print(color.GREEN + "Correct !" + color.RESET)
                    seen.add(char.kana)
                    score += 1
            else :
                
                duplicates[char.kana] += 1
                failed += 1

                print(color.RED + "Your answer is incorrect" + color.RESET)
                print(f"The {quetion} : {char.kana}")
                print(f"Romaji : {char.romaji}")

        real_duplicates = [i for i,f  in duplicates.items() if f > 1]

        tl_duplicates = sum(duplicates[i] for i in real_duplicates) - len(real_duplicates)

        unique_attempts = shown - tl_duplicates

        if unique_attempts > 0:
            fail_rate = (failed / unique_attempts) * 100
        else:
            fail_rate = (failed / shown) * 100

        succes_rate = 100 - fail_rate

        if tl_duplicates :
            print(f"Number of repeated kana : {tl_duplicates}")

        print(f"Success rate {succes_rate: .2f}")
        print(f"Fail rate {fail_rate: .2f}")

        return


    def quizzer_hira(self) :
        self.quizzer("hiragana")

    def quizzer_kata(self) :
            self.quizzer("katakana")

    
        








    