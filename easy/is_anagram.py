# 2つの文字列がアナグラム(文字の並び順は違っても、使われている文字と数が同じ文字列)か判定する
# 時間計算量: O(n) n は文字列の長さ
# 空間計算量: O(k) k は文字の種類数。通常は最大でも文字種の数なので、実質 O(1) と考える場合もある
def is_anagram(s, t):
    # 文字列をソートして比較することで、アナグラムかどうかを判定します
    return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
print(is_anagram(s, t))
s = "rat"
t = "car"
print(is_anagram(s, t))

