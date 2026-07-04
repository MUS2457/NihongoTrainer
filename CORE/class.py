class Kotoba:
    def __init__(self, word, romaji, meaning, example=None):
        self.word = word
        self.romaji = romaji
        self.meaning = meaning
        self.example = example
        self.level = 0
        self.next_review = None

    def to_dict(self):
        return {
            "word": self.word,
            "romaji": self.romaji,
            "meaning": self.meaning,
            "example": self.example,
            "level": self.level,
            "next_review": self.next_review
        }
