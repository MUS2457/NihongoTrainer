import random
from STORAGE.storage import load_db, save_db

class Quiz :
    def __init__(self) :
        self.db = load_db()
    
    def save(self) :
        save_db(self.db)

    
    def guess_meaning(self) :
        count = 0
        duplicate = []
        interval = min(len(self.db), 15)

        while count <= interval :

            w = random.choice(self.db)
            duplicate.append(w["word"])
            
            print(f"what is the meaning of the following word {w["word"]}")

            ansewer = input("enter your answer").strip()

            if ansewer == w["meaning"] :
                if w["word"] not in duplicate :
                    print("your answer is correct")
                    count += 1
                else :
                    pass

            else :
                print("your answer is incorrect")
                count -= 1


