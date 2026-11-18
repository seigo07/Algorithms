
# 文字列 s の文字を並べ替えて作れる、最長の回文の長さを求める
# 例：s = "abccccdd" → 7

# - 回文では、左右に同じ文字を配置する。
# - 偶数個の文字はすべて使用できる。
# - 奇数個の文字は1個だけ中央に配置できる。
# - 大文字・小文字は区別する。

# 1. 各文字の出現回数を数える
# 2. 各文字について、使用できる最大の偶数個を加算する
# 3. 奇数個の文字が存在すれば、中央用に1を加算する
# 4. 最長の回文の長さを返す

# 時間計算量：O(n) 空間計算量：O(k) kは文字種類

from collections import Counter

def longest_palindrome(s):
    counts = Counter(s)  # 各文字の出現回数
    result = 0           # 回文の長さ

    for count in counts.values():
        result += (count // 2) * 2  # 使用できる偶数個を加算

    if result < len(s):
        result += 1  # 奇数個の文字を中央に1つ配置

    return result


test_cases = [
    ("abccccdd", 7),
    ("a", 1),
    ("Aa", 1),       # 大文字と小文字は別の文字
    ("aabb", 4),
    ("abc", 1),
]

for s, expected in test_cases:
    result = longest_palindrome(s)

    print(f"入力: {s}")
    print(f"結果: {result}")
    print()
