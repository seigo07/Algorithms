# anagram同士をまとめる
# 時間計算量: 時間計算量: O(n × k log k) 文字列の数を n、1つの文字列の平均長を kとする sorted(s) = O(k log k) * n
# 空間計算量: O(n × k) すべての文字列を辞書に保持
from collections import defaultdict

def group_anagrams(strs):
    # key: ソートした文字列
    # value: 同じアナグラムの文字列一覧
    # ex. "aet": ["eat", "tea", "ate"]
    groups = defaultdict(list)

    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)

    return list(groups.values())


# 実行例
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))