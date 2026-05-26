# magazine内の文字からransom_noteが作成可能かどうか
# 時間計算量: O(n + m) n = len(ransomNote)
# 空間計算量: O(m) m = len(magazine)
from collections import Counter

def can_construct(ransom_note, magazine):
    # magazine内の各文字の残り回数を数える
    # e.g. {'a': 3, 'b': 3, 'c': 2}
    count = Counter(magazine)

    # ransom_noteの文字を1つずつ使えるか確認
    for ch in ransom_note:
        if count[ch] == 0:
            return False  # 必要な文字が足りない
        count[ch] -= 1    # 文字を1つ消費

    return True


# 例の実行
ransom_note = "aabb"
magazine = "aaabbbcc"
result = can_construct(ransom_note, magazine)
print(result)  # True
