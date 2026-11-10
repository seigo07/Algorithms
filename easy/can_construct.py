
# magazine内の文字からransom_noteが作成可能かどうか

# 1. magazine に含まれる各文字の出現回数を記録する。
# 2. ransomNote の文字を1文字ずつ取り出す。
# 3. 必要な文字が残っているか確認する。
# 4. 足りなければ False、足りていればその文字の残り個数を1減らす。
# 5. 最後まで確認できれば True を返す。

# 時間計算量: O(n + m)
# 空間計算量: O(k) magazine に出てくる文字の種類数
# n = ransomNoteの文字数 m = magazineの文字数 ex. magazine = "aab" → m=3, k=2 ransomNote = "aa" → n=2

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
