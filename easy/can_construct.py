# ransomNoteの各文字がmagazineから取得可能な場合はTrueを返し、それ以外の場合はFalseを返す


def can_construct(ransomNote, magazine):
    # magazine内の各文字の出現回数をカウントするdic
    # e.g. {'a': 3, 'b': 3, 'c': 2}
    magazine_count = {}
    for char in magazine:
        # charがmagazine内に存在しない場合0を返し、文字の出現回数を1に設定
        # それ以外の場合、文字の出現回数をインクリメント
        magazine_count[char] = magazine_count.get(char, 0) + 1

    # ransomNote内の各文字の出現回数をカウントし、magazine内の文字を使用して構築できるか判定
    for char in ransomNote:
        # 辞書に文字の登録がない場合
        if char not in magazine_count or magazine_count[char] == 0:
            return False
        magazine_count[char] -= 1

    # 辞書内の文字が使い切られていない場合
    return True


# 例の実行
ransom_note = "aabb"
magazine = "aaabbbcc"
result = can_construct(ransom_note, magazine)
print(result)  # True
