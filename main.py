from CORE import quiz, word_manager
from STORAGE import storage

manager = word_manager.KotobaManager()
study = quiz.Quiz()

def manage_word() :
    while True :

        print("1. Add kotoba")
        print("2. Delete word")
        print("3. Update word")

        choice = input("Enter your choice based on number from the menu, or 'q' to quit :").strip()

        if choice.lower() == "q":
            print("back to main menu")
            return
            
        elif not choice.isdigit() or int(choice) not in [1, 2, 3] :
            print("invalid input")
            continue

        confirm = int(choice)

        if confirm == 1 :
            manager.add_kotoba()

        elif confirm == 2 :
            if not manager.db :
                print("No words to Delete")
                continue

            manager.delete_kotoba()

        else :
            if manager.db :
                manager.Update_kotoba()

            else :
                print("No words to Update")
                continue


def test_review() :
    if not study.db :
        print("No words for review or  for taking a quiz nor for search")
        return
    
    while True :
    
        print("1. Review words")
        print("2. Take quiz")
        print("3. search a word (s)")

        choice = input("Enter your choice based on number from the menu or 'q'").strip()

        if choice == "q" :
            print("back to main menu")
            return

        elif not choice.isdigit() or int(choice) not in [1, 2, 3] :
            print("invalid input")
            continue

        confirm = int(choice)

        if confirm == 1 :
            manager.review_kotoba()

        elif confirm == 2 :
            while True :

                print("1. guess by meaning")
                print("2. guess the kana based on romaji")
                print("3. back to the first menu")

                user = input("Enter your choice based on number from the menu or 'q'").strip()

                if not user.isdigit() or int(user) not in [1, 2, 3] :
                    print("invalid input")
                    continue

                user2 = int(user)

                if user2 == 1 :
                    study.guess_meaning()

                elif user2 == 2 :
                    study.guess_word()

                else :
                    print("back to menu")
                    break
        
        else :
            manager.search_kotoba()
        
