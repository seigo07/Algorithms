# 重なっている区間を1つにまとめる
# 時間計算量: O(n log n) ← ソート
# 空間計算量: O(n) ← 結果 merged

def merge(intervals):
    intervals.sort()    # index0の要素で昇順ソート
    merged = []

    for start, end in intervals:
        # 最初の区間 or 前の区間と重ならない
        # merged[-1][1]は最後の配列のindex1の要素
        if not merged or merged[-1][1] < start:
            merged.append([start, end])

        # 重なる場合、終了位置を広げる ex. [1,3][2,6] → [1,6]
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged


intervals = [[1,3], [2,6], [8,10], [15,18]]
print(merge(intervals))