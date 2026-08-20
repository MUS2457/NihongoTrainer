from QUIZ import word_manager, word_quiz, kana_quiz
import sys

from STORAGE import kana_storage

manager = word_manager.KotobaManager()
study = word_quiz.KotobaQuizzer()
kana = kana_quiz.KanaManager()

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
                print("3. guess the romaji based on kana")
                print("4. take quiz in hiragana")
                print("5. take quiz in katakana")
                print("0. back to the first menu")

                user = input("Enter your choice based on number from the menu : ").strip()

                if not user.isdigit() or int(user) not in [0, 1, 2, 3, 4,5] :
                    print("invalid input")
                    continue

                user2 = int(user)

                if user2 == 1 :
                    study.quizzer_meaning()

                elif user2 == 2 :
                    study.quizzer_romanji()

                elif user2 == 3 :
                    study.quizzer_kana()

                elif user2 == 0 :
                    print("back to menu")
                    break

                elif user2 == 4 :
                    kana.quizzer_hira()

                else :
                    kana.quizzer_kata()
        
        else :
            manager.search_kotoba()
        
def program () :
    while True :
        print("1. manage kotoba (add, update...ect) ")
        print("2. study (review, quiz)")
        print("0. exit")

        choice = input("Enter a number from the menu").strip()

        if not choice.isdigit() or int(choice) not in [0, 1, 2] :
            print("Invalid input")
            continue

        x = int(choice)

        if x == 0 :
            print("Goodbye , program will close")
            sys.exit()

        elif x == 1 :
            manage_word()

        elif x == 2 :
            test_review()


if __name__ == "__main__" :
       program()
       
       