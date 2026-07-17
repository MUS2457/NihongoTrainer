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
        deplicate_counter = 0

        while count < interval : #< prevent runnig 16 times

            w = random.choice(self.db)
            
            print(f"what is the meaning of the following word {w["word"]}")

            answer = input("Enter your answer").strip()

            if answer == w["meaning"] :
                if w["word"] not in duplicate :
                    duplicate.append(w["word"])
                    print("your answer is correct")
                    count += 1
                    
                else :
                    deplicate_counter += 1

            else :
                print("your answer is incorrect")
                print(f"the correct meaning : {w['meaning']}")
                print(f"Romaji : {w['romaji']}")
                print(f"Example : {w.get('example', 'use update tool to add example for better understanding !')}")
                count -= 1

        print(f"{interval} has been reviwed !, number of word shown more than 1 time {deplicate_counter}")
        return



