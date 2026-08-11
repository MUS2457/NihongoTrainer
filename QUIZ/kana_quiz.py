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

    def build_attribute (self, obj, word) :
        return getattr(obj, word)

    def quizzer (self, quetion, answer) :
        score = 0
        showed = 0
        failed = 0
        duplicates = collections.defaultdict(int)
        seen = set()

        while score < 15 :
            char = random.choice(getattr(self,quetion))
            showed += 1

            user = input(f"Enter the {answer} corresponding to this {char.kana} ").strip()

            if user.lower() == char.romaji :
                if char.kana in seen :
                    duplicates[char.kana] += 1
                    

                else :
                    seen.add(char.kana)
                    score += 1

            else :
                failed += 1










    