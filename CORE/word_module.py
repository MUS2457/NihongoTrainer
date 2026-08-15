class Kotoba:
    def __init__(self, word, romaji, meaning, example=None, level=1, next_review=None):
        self.word = word
        self.romaji = romaji
        self.meaning = meaning
        self.example = example
        self.level = level
        self.next_review = next_review

    def to_dict(self):
        return {
            "word": self.word,
            "romaji": self.romaji,
            "meaning": self.meaning,
            "example": self.example,
            "level": self.level,
            "next_review": self.next_review
        }

    @classmethod
    def from_dict(cls, dict) :
        return cls(
            word = dict["word"],
            romaji = dict["romaji"],
            meaning = dict["meaning"],
            example = dict["example"],
            level = dict["level"],
            next_review = dict["next_review"]
        )

    def __str__(self):
        example = self.example or "No example provided"
        return (
        f"Word       : {self.word}\n"
        f"Romaji     : {self.romaji}\n"
        f"Meaning    : {self.meaning}\n"
        f"Example    : {example}\n"
        f"Level      : {self.level}\n"
        f"NextReview : {self.next_review}"
    )
