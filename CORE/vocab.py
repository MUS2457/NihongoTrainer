from STORAGE import storage

def add_kotoba() :
    print("add new word")
    while True :
        word = input("your word in hira or kata").strip()
        if not word :
            print("Enter a word")
            continue

        romanji = input("the word in alphabet").strip()
        if not romanji :
            print("no romanji provided")
            continue

        meaning = input("Enter the meaning of it")

        if not meaning :
            print("you forget to type the mean")
            continue

        example = input("enter an example (optinal)")

        return ""

    


        
