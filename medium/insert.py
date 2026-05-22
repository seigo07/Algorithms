# ソート済み・重複なし区間リストに new_interval を挿入し、重なる区間をマージする
# 時間空間計算量: O(n)
def insert(intervals, new_interval):
    result = []
    start, end = new_interval

    for i, (s, e) in enumerate(intervals):
        # new_interval が今の区間より前にある → ここで挿入確定
        if end < s:
            i -= 1
            break
        # new_interval が今の区間と重複 → new_interval を広げる
        elif start <= e:
            start = min(start, s)
            end = max(end, e)
        # new_interval が今の区間より後ろ → そのまま追加
        else:
            result.append([s, e])

    return result + [[start, end]] + intervals[i+1:]


intervals = [[1,3],[6,9]]
new_interval = [2,5]
print(insert(intervals, new_interval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval = [4,8]
print(insert(intervals, new_interval))
