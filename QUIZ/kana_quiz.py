from STORAGE import kana_storage
from CORE import kana_module
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
        showed = 0
        failed = 0
        duplicates = collections.defaultdict(int)
        seen = set()

        while score < 20 :
            char = random.choice(getattr(self,quetion))
            showed += 1

            user = input(f"Enter the 'Romaji' corresponding to this {char.kana} ").strip()

            if user.lower() == char.romaji :

                if char.kana is seen :
                    duplicates[char.kana]

                else :
                    seen.add(char.kana)
                    score += 1
            else :
                duplicates[char.kana] += 1
                failed += 1

                print("Your answer is incorrect !")
                print(f"The {quetion} : {char.kana}")
                print(f"Romaji : {char.romaji}")

        real_duplicates = [i for i,f  in duplicates.items() if f > 1]

        tl_duplicates = sum(duplicates[i] for i in real_duplicates) - len(real_duplicates)

        fail_rate = (failed / (showed - tl_duplicates)) * 100
        succes_rate = 100 - fail_rate

        if tl_duplicates :
            print(f"Number of repeated kana : {tl_duplicates}")

        print(f"Success rate {succes_rate: .2f}")
        if fail_rate :
            print(f"Fail rate {fail_rate: .2f}")

        else :
            print(f"Perfect score you are a best ,Keep going")

        return


    def quizzer_hira(self) :
        self.quizzer("hiragana")

    def quizzer_kata(self) :
            self.quizzer("katakana")
        








    