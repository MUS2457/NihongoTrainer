test_words = [
    {
        "word": "猫",
        "romaji": "neko",
        "meaning": "cat",
        "example": "猫が好きです。",
        "level": 0,
        "next_review": "2026-07-16"
    },
    {
        "word": "食べる",
        "romaji": "taberu",
        "meaning": "to eat",
        "example": "寿司を食べる。",
        "level": 1,
        "next_review": "2026-07-16"
    },
    {
        "word": "速い",
        "romaji": "hayai",
        "meaning": "fast",
        "example": "彼は走るのが速い。",
        "level": 3,
        "next_review": "2026-07-16"
    },
    {
        "word": "勉強",
        "romaji": "benkyou",
        "meaning": "study",
        "example": "日本語を勉強しています。",
        "level": 5,
        "next_review": "2026-07-16"
    },
    {
        "word": "水",
        "romaji": "mizu",
        "meaning": "water",
        "example": "水を飲みます。",
        "level": 2,
        "next_review": "2026-07-16"
    }
]

def review_kotoba() :
        print("==Review words==")
        
        words = test_words
        remaining = len(words)

        if not words :
            print("No words are due for review.")
            return
        
        print(f"You have {len(words)} words due for review:")

        for w in words :
            print(f"Remaining words : {remaining}")
            remaining -= 1

            print(f"{w['word']} ({w['romaji']}) - {w['meaning']}")
            if w.get("example") :
                print(f"Example: {w['example']}")
            
            input("Press Enter to continue to the next word...")

            familiarity = list(("Completely", "Partially", "Not at all"))
            
            while True :
                print("==Familiarity scale==")
                for i, l in enumerate(familiarity, start = 1) :
                    print(f"{i}. {l}")
                    
                remember = input("Enter a number from (1 to 3) based on familiarity scale").strip()

                if not remember.isdigit() or int(remember) not  in [1,2,3] :
                    print("Invalid choice")
                    continue

                index = int(remember) -1 

                if familiarity[index] == "Completely" :
                    w["level"] += 1

                elif familiarity[index] == "Partially" :
                    w["level"] = max(0, w["level"] - 1)

                else :
                    w["level"] = 0
            
                w["next_review"] = self.calculate_next_review(w["level"])


if __name__ == "__main__":
    review_kotoba()
    