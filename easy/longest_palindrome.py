# 最長の回文の長さを求める。大文字と小文字は別の文字として扱う
# 時間計算量：O(n) 空間計算量：O(k) kは文字種類

from collections import Counter

def longest_palindrome(s):
    counts = Counter(s)
    length = sum(count // 2 * 2 for count in counts.values())
    if length < len(s):
        length += 1
    return length


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
