class Kana:
    def __init__(self, kana, romaji, type):
        self.kana = kana
        self.romaji = romaji
        self.type = type

    def to_dict(self):
        return {
            "kana": self.kana,
            "romaji": self.romaji,
            "type": self.type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            kana=data["kana"],
            romaji=data["romaji"],
            type=data["type"]
        )
