# 単語配列 words から、出現回数が多い上位 k 個の単語を取得
# 出現回数が多い単語順 出現回数が同じなら辞書順
# 時間計算量: O(n + m log m) Counter(words): O(n) + sorted(...): O(m log m)
# 空間計算量: O(m) n = wordsの要素数、m = 単語の種類の数

from collections import Counter

def top_k_frequent(words, k):
    count = Counter(words)
    sorted_words = sorted(count, key=lambda w: (-count[w], w)) # 降順・辞書順
    return sorted_words[:k]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(top_k_frequent(words, k))