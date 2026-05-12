# 文字列の中で、重複なしの最長部分文字列の長さを求める(abcabcbb→abcの3)
# 時間: O(n) 空間: O(n) 各文字を最大2回しか見ないので高速
def lengthOfLongestSubstring(s):
    used = {}      # 各文字: 最後に出たindex {‘a’:0,‘b’:1,‘c’:2}
    left = 0       # 「重複なし部分文字列」の左端index
    max_len = 0
    for right in range(len(s)):
        char = s[right]
        if char in used and used[char] >= left:
            left = used[char] + 1   # 重複したら左indexを+1ずらず
        used[char] = right  # 各文字を最後に出たindexに更新
        max_len = max(max_len, right - left + 1)    # 現在の重複なしの最長部分文字列の長さを更新
    return max_len


# 使用例
strings = ["abcabcbb", "bbbbb", "pwwkew", ""]

for s in strings:
    print(f"String: {s}")
    print(f"Longest substring without repeating characters: {lengthOfLongestSubstring(s)}\n")
