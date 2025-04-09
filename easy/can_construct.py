
# ransom_noteがmagazineの文字を使って構成可能かを判定

from collections import Counter


def can_construct(ransom_note, magazine):

    # 各文字の出現回数をカウント
    # e.g. {'a': 3, 'b': 3, 'c': 2}
    ransom_count = Counter(ransom_note)
    magazine_count = Counter(magazine)

    print(ransom_count)
    print(magazine_count)

    # 各文字の必要数が magazine に足りているか確認
    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            # 一文字でも足りなければFalse
            return False
    # すべての文字が足りていればTrue
    return True

# 例の実行
ransom_note = "aabb"
magazine = "aaabbbcc"
result = can_construct(ransom_note, magazine)
print(result)  # True
