
# 2つの文字列 s と t がアナグラムかどうかを判定

def is_anagram(s, t):
    # 文字列 s, t を1文字ずつ分解し、昇順に並べる
    return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
print(is_anagram(s, t))
s = "rat"
t = "car"
print(is_anagram(s, t))

