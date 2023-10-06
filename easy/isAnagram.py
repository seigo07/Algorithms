# 与えられた2つの文字列 s と t がアナグラムであるかどうかを判定する
# アナグラムとは、異なる単語やフレーズの文字を並び替えて、
# 元の文字をすべて正確に一度ずつ使用して新しい単語やフレーズを作成すること


def isAnagram(s, t):
    # 文字列をソートして比較することで、アナグラムかどうかを判定します
    return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
s = "rat"
t = "car"
print(isAnagram(s, t))

