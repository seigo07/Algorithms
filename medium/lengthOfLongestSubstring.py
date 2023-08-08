# 文字列 s が与えられた場合、最も長い文字列の長さを見つけます。
# 部分文字列文字を繰り返さずに。

# このプログラムは、与えられた文字列 s の中で最も長い部分文字列（substring）の長さを返す関数 lengthOfLongestSubstring を定義しています。
# その部分文字列は、重複する文字を含んでいません。
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        set_chars = set()
        ans = 0
        i, j = 0, 0
        while i < n and j < n:
            # 文字がsetにない場合、その文字を追加してjを進める
            if s[j] not in set_chars:
                set_chars.add(s[j])
                j += 1
                ans = max(ans, j - i)
            # そうでない場合、setからs[i]を削除してiを進める
            else:
                set_chars.remove(s[i])
                i += 1
        return ans


# インスタンスの作成
solution = Solution()

# 使用例
strings = ["abcabcbb", "bbbbb", "pwwkew", ""]

for s in strings:
    print(f"String: {s}")
    print(f"Longest substring without repeating characters: {solution.lengthOfLongestSubstring(s)}\n")
