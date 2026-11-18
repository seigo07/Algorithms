
# 重なっている区間を1つにまとめる

# 1. ソート：区間を開始位置の昇順に並べる。
# 2. 比較：現在の区間と直前の区間が重複するか確認する。
# 3. 結合：重複していれば終了位置を更新する。
# 4. 追加：重複していなければ新しい区間として追加する。
# 5. 返却：結合済みの区間一覧を返す。

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