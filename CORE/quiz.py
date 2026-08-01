import random
from STORAGE.storage import load_db, save_db

class Quiz :
    def __init__(self) :
        self.db = load_db()
    
    def save(self) :
        save_db(self.db)

    
    def guessing(self, question, answers) :
        count = 0
        interval = min(len(self.db), 15)
        duplicates = {}
        showns = 0
        failes = 0
        failures = []

        while count < interval : #< prevent runnig 16 times start at 0

            w = random.choice(self.db)
            showns += 1
            
            print(f"what is the {answers} of the following {w[question]} :")

            answer = input("Enter your answer : ").strip()

            if answer == w[answers] :

                if w[question] not in duplicates :

                    duplicates[w[question]] = 0
                else :

                    duplicates[w[question]] += 1

                    if len(self.db) >= 10 :
                        count -=1
                
                
                count += 1
                
            else :
                duplicates[w[question]] = duplicates.get(w[question], 0) +1
                print("your answer is incorrect")
                print(f"the correct meaning : {w[answers]}")
                print(f"Romaji : {w['romaji']}")
                print(f"Example : {w.get('example', 'use update tool to add example for better understanding !')}")

                count -= 1
                failes += 1
                failures.append(w[question])


        real_duplicates = []

        for w in duplicates.keys() :
            if duplicates[w] != 1 :
                real_duplicates.append(w)

        only_duplicates = sum(duplicates[k] for k in real_duplicates) - len(real_duplicates)
        
        print(f"{showns} has been reviwed in total!1, number of word shown more than 1 time {abs(only_duplicates)}")

        if failures :
                    failed , results = self.failed_words(failures, question)
                    percentage_fail = (failes / showns) * 100

                    print("== max failed word ==")
                    print(f"word : {failed["word"]}")
                    print(f"Romaji : {failed["romaji"]}")
                    print(f"Meaning : {failed["meaning"]}")
                    print(f"Example : {failed.get("example", "No example provided")}")
         
                    others = [i for i in results if i != failed]
         
                    if others:
                        print("\nOther failed words:")
                        for item in others:
                            
                            print(f"word : {item["word"]}")
                            print(f"Romaji : {item["romaji"]}")
                            print(f"Meaning : {item["meaning"]}")
                            print(f"Example : {item.get("example", "No example provided")}")
                            print("=" * 40)                

                    print(f"fail percentage : {percentage_fail} % ")
        return 
        
    
    def guess_meaning(self) :
        self.guessing(question= "word", answers= "meaning")

    def guess_word(self) :
        self.guessing(question= "romaji", answers= "word")
    
    def failed_words(self, failures, question) :
        counter = {}
        for w in failures :
            counter[w] = counter.get(w, 0) + 1

        max_failed = max(counter , key = counter.get)
        results = [w for w in self.db if w[question] in failures]

        failed = next(w for w in self.db if w["word"] == max_failed)  # next make it a varible instead of generator
        return failed, results


