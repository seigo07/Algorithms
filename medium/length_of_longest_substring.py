# 文字列の中で、重複なしの最長部分文字列の長さを求める(abcabcbb→abcの3)
# 時間計算量: O(n)
# 空間計算量: O(min(n, 文字種類数)) 重複していない文字を chars に保存するため
def length_of_longest_substring(s):
    chars = set()
    left = 0
    max_len = 0

    for right, c in enumerate(s):
        # c が重複している間、左から文字を削除
        while c in chars:
            chars.remove(s[left])
            left += 1

        chars.add(c)
        max_len = max(max_len, right - left + 1)

    return max_len

# 使用例
strings = ["abcabcbb", "bbbbb", "pwwkew", ""]

for s in strings:
    print(f"String: {s}")
    print(f"Longest substring without repeating characters: {length_of_longest_substring(s)}\n")
