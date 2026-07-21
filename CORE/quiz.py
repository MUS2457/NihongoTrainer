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

        while count < interval : #< prevent runnig 16 times start at 0

            w = random.choice(self.db)
            showns += 1
            
            print(f"what is the {answers} of the following  {w[question]}")

            answer = input("Enter your answer").strip()

            if answer == w[answers] :
                if question not in duplicates :

                    duplicates[w[question]] = 0
                duplicates[w[question]] += 1
                
            else :
                print("your answer is incorrect")
                print(f"the correct meaning : {w[answers]}")
                print(f"Romaji : {w['romaji']}")
                print(f"Example : {w.get('example', 'use update tool to add example for better understanding !')}")
                count -= 1

        for w in duplicates.keys() :
            if duplicates[w] == 1 :
                del duplicates[w]

        only_duplicates = sum(count for count in duplicates.values()) - len(duplicates)
        failed , results = self.failed_words(duplicates)
        percentage_fail = (sum(duplicates.values()) / showns) * 100

        if results :
            print(f"Most failed {question} :")
            print(f"word : {failed['word']} ")
            print(f"romaji : {failed['romaji']}")
            print(f"example : {failed.get('example', 'no example provided')}")
 
            others = [i for i in results if  i != failed ]

            if others:
                print("\nOther failed words:")
                for item in others:
                    print(item)
        
        print(f"{showns} has been reviwed in total!, number of word shown more than 1 time {only_duplicates}")
        print(f"fail percentage : {percentage_fail} % ")
             
        return 
        
    
    def guess_meaning(self) :
        self.guessing(question= "word", answers= "meaning")

    def guess_word(self) :
        self.guessing(question= "romaji", answers= "word")
    
    def failed_words(self, duplicates) :
        failedWords = [i for i,f in duplicates.items() if f >= 2]
        max_fail = max(duplicates, key = duplicates.get)
        results = [w for w in self.db if w["word"] in failedWords ]
        failed = next(w for w in self.db if w["word"] == max_fail)  # next make it a varible instead of generator
        return failed, results


