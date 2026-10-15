# ソート済み・重複なし区間リストに new_interval を挿入し、重なる区間をマージする
# 1. 左側：新しい区間より前 → そのまま追加
# 2. 右側：新しい区間より後 → そのまま追加（ここで挿入確定）
# 3. 重複：それ以外、新しい区間と重なる → min()、max() で結合
# 時間空間計算量: O(n)
def insert(intervals, new_interval):
    result = []
    for i, interval in enumerate(intervals):
        # 1. 左側：新しい区間より前 → そのまま追加
        if interval[1] < new_interval[0]:
            result.append(interval)
        # 2. 右側：新しい区間より後 → そのまま追加（ここで挿入確定）
        elif interval[0] > new_interval[1]:
            return result + [new_interval] + intervals[i:]
        # 3. 重複：それ以外、新しい区間と重なる → min()、max() で結合
        else:
            new_interval[0] = min(interval[0],new_interval[0])
            new_interval[1] = max(interval[1],new_interval[1])
    return result + [new_interval]


intervals = [[1,3],[6,9]]
new_interval = [2,5]
print(insert(intervals, new_interval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval = [4,8]
print(insert(intervals, new_interval))
