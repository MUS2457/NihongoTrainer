import csv
import os

kana_list = [
    # --- Hiragana ---
    ("あ","a","hiragana"), ("い","i","hiragana"), ("う","u","hiragana"),
    ("え","e","hiragana"), ("お","o","hiragana"),

    ("か","ka","hiragana"), ("き","ki","hiragana"), ("く","ku","hiragana"),
    ("け","ke","hiragana"), ("こ","ko","hiragana"),

    ("さ","sa","hiragana"), ("し","shi","hiragana"), ("す","su","hiragana"),
    ("せ","se","hiragana"), ("そ","so","hiragana"),

    ("た","ta","hiragana"), ("ち","chi","hiragana"), ("つ","tsu","hiragana"),
    ("て","te","hiragana"), ("と","to","hiragana"),

    ("な","na","hiragana"), ("に","ni","hiragana"), ("ぬ","nu","hiragana"),
    ("ね","ne","hiragana"), ("の","no","hiragana"),

    ("は","ha","hiragana"), ("ひ","hi","hiragana"), ("ふ","fu","hiragana"),
    ("へ","he","hiragana"), ("ほ","ho","hiragana"),

    ("ま","ma","hiragana"), ("み","mi","hiragana"), ("む","mu","hiragana"),
    ("め","me","hiragana"), ("も","mo","hiragana"),

    ("や","ya","hiragana"), ("ゆ","yu","hiragana"), ("よ","yo","hiragana"),

    ("ら","ra","hiragana"), ("り","ri","hiragana"), ("る","ru","hiragana"),
    ("れ","re","hiragana"), ("ろ","ro","hiragana"),

    ("わ","wa","hiragana"), ("を","wo","hiragana"), ("ん","n","hiragana"),

    # --- Hiragana Dakuten ---
    ("が","ga","hiragana"), ("ぎ","gi","hiragana"), ("ぐ","gu","hiragana"),
    ("げ","ge","hiragana"), ("ご","go","hiragana"),

    ("ざ","za","hiragana"), ("じ","ji","hiragana"), ("ず","zu","hiragana"),
    ("ぜ","ze","hiragana"), ("ぞ","zo","hiragana"),

    ("だ","da","hiragana"), ("ぢ","ji","hiragana"), ("づ","zu","hiragana"),
    ("で","de","hiragana"), ("ど","do","hiragana"),

    ("ば","ba","hiragana"), ("び","bi","hiragana"), ("ぶ","bu","hiragana"),
    ("べ","be","hiragana"), ("ぼ","bo","hiragana"),

    # --- Hiragana Handakuten ---
    ("ぱ","pa","hiragana"), ("ぴ","pi","hiragana"), ("ぷ","pu","hiragana"),
    ("ぺ","pe","hiragana"), ("ぽ","po","hiragana"),

    # --- Small Hiragana ---
    ("ゃ","ya","hiragana-small"), ("ゅ","yu","hiragana-small"),
    ("ょ","yo","hiragana-small"),
    ("ぁ","a","hiragana-small"), ("ぃ","i","hiragana-small"),
    ("ぅ","u","hiragana-small"), ("ぇ","e","hiragana-small"),
    ("ぉ","o","hiragana-small"),
    ("っ","tsu","hiragana-small"),

    # --- Katakana ---
    ("ア","a","katakana"), ("イ","i","katakana"), ("ウ","u","katakana"),
    ("エ","e","katakana"), ("オ","o","katakana"),

    ("カ","ka","katakana"), ("キ","ki","katakana"), ("ク","ku","katakana"),
    ("ケ","ke","katakana"), ("コ","ko","katakana"),

    ("サ","sa","katakana"), ("シ","shi","katakana"), ("ス","su","katakana"),
    ("セ","se","katakana"), ("ソ","so","katakana"),

    ("タ","ta","katakana"), ("チ","chi","katakana"), ("ツ","tsu","katakana"),
    ("テ","te","katakana"), ("ト","to","katakana"),

    ("ナ","na","katakana"), ("ニ","ni","katakana"), ("ヌ","nu","katakana"),
    ("ネ","ne","katakana"), ("ノ","no","katakana"),

    ("ハ","ha","katakana"), ("ヒ","hi","katakana"), ("フ","fu","katakana"),
    ("ヘ","he","katakana"), ("ホ","ho","katakana"),

    ("マ","ma","katakana"), ("ミ","mi","katakana"), ("ム","mu","katakana"),
    ("メ","me","katakana"), ("モ","mo","katakana"),

    ("ヤ","ya","katakana"), ("ユ","yu","katakana"), ("ヨ","yo","katakana"),

    ("ラ","ra","katakana"), ("リ","ri","katakana"), ("ル","ru","katakana"),
    ("レ","re","katakana"), ("ロ","ro","katakana"),

    ("ワ","wa","katakana"), ("ヲ","wo","katakana"), ("ン","n","katakana"),

    # --- Katakana Dakuten ---
    ("ガ","ga","katakana"), ("ギ","gi","katakana"), ("グ","gu","katakana"),
    ("ゲ","ge","katakana"), ("ゴ","go","katakana"),

    ("ザ","za","katakana"), ("ジ","ji","katakana"), ("ズ","zu","katakana"),
    ("ゼ","ze","katakana"), ("ゾ","zo","katakana"),

    ("ダ","da","katakana"), ("ヂ","ji","katakana"), ("ヅ","zu","katakana"),
    ("デ","de","katakana"), ("ド","do","katakana"),

    ("バ","ba","katakana"), ("ビ","bi","katakana"), ("ブ","bu","katakana"),
    ("ベ","be","katakana"), ("ボ","bo","katakana"),

    # --- Katakana Handakuten ---
    ("パ","pa","katakana"), ("ピ","pi","katakana"), ("プ","pu","katakana"),
    ("ペ","pe","katakana"), ("ポ","po","katakana"),

    # --- Small Katakana ---
    ("ャ","ya","katakana-small"), ("ュ","yu","katakana-small"),
    ("ョ","yo","katakana-small"),
    ("ァ","a","katakana-small"), ("ィ","i","katakana-small"),
    ("ゥ","u","katakana-small"), ("ェ","e","katakana-small"),
    ("ォ","o","katakana-small"),
    ("ッ","tsu","katakana-small")
]

ROOT = os.path.dirname(os.path.dirname(__file__))  # go up from STORAGE , __file__ represent current position
DB_DIR = os.path.join(ROOT, "DB")  # dirname == back one step path name ex :ftp/db/csv after become ftp/db
file_path = os.path.join(DB_DIR, "kana.csv")


def save_kana() :

    os.makedirs(DB_DIR, exist_ok=True)  

    with open(file_path, "w", encoding = "utf-8", newline= "") as kana :
        writer = csv.writer(kana)
        writer.writerow(["kana", "romaji", "type"])
        writer.writerows(kana_list)


def load_kana() :

    if not os.path.isfile(file_path) :
        save_kana()

    try :
        with open(file_path, "r") as kana :
            reader = csv.DictReader(kana)
            return list(reader)  #list of dic

    except Exception as e :
        print("Error loading kana", e)
        return []

    



