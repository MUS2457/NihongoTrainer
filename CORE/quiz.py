import random
from STORAGE.storage import load_db, save_db

class Quiz :
    def __init__(self) :
        self.db = load_db()
    
    def save(self) :
        save_db(self.db)

    
    def guess_meaning(self) :
        count = 0
        interval = min(len(self.db), 15)
        duplicates = {}
        showns = 0

        while count < interval : #< prevent runnig 16 times start at 0

            w = random.choice(self.db)
            showns += 1
            
            print(f"what is the meaning of the following word {w["word"]}")

            answer = input("Enter your answer").strip()

            if answer == w["meaning"] :
                if w["word"] not in duplicates :

                    duplicates[w["word"]] = 0
                duplicates[w["word"]] += 1
                
            else :
                print("your answer is incorrect")
                print(f"the correct meaning : {w['meaning']}")
                print(f"Romaji : {w['romaji']}")
                print(f"Example : {w.get('example', 'use update tool to add example for better understanding !')}")
                count -= 1

        for w in duplicates.keys() :
            if duplicates[w] == 1 :
                del duplicates[w]
        
        only_duplicates = sum(count for count in duplicates.values()) - len(duplicates)

        print(f"{showns} has been reviwed in total!, number of word shown more than 1 time {only_duplicates}")
        return



