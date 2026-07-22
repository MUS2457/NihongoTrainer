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



    except ValueError :
        print("invalid input")
        manage_word()


def test_review() :
    if not study.db :
        print("No words for review or taking a quiz nor for search")
        return
    
    while TRue
    
    print("1. Review words")
    print("2. Take quiz")
    print("3. search a word (s)")
    print("4. exit")

    try :
        choice = int(input("Enter your choice based on number from the menu"))

        if choice == 1 :
            manager.review_kotoba()

        elif choice == 2 :
            print("1. guess by meaning")
            print("2. guess the kana based on romaji")
            print("3. exit")
            
            try :
                user = int(input("Enter your choice based on number from the menu"))

                if user == 1 :
                    study.guess_meaning()

                elif user == 2 :
                    study.guess_word()

                elif user == 3 :
                    print("back to main menu")
                    return
            
            except ValueError :
                print("invalid input")
                return
        
        elif choice == 3 :
            manager.search_kotoba()

        elif choice == 4 :
            print("back to main menu")
            return
        
    except ValueError :
        test_review()



