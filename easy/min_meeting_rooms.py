# すべての会議を開催するために必要な最小会議室数を求める
# 時間計算量：O(n log n) ソート 各会議に対するヒープ操作
# 空間計算量：O(n)
import heapq
def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    # 会議を開始時刻順でsort
    intervals.sort()
    # 使用中の会議室について、各会議の終了時刻を保存する最小ヒープ
    end_times = []
    for start, end in intervals:
        # 最も早く終了する会議が、現在の会議開始前に終わっていれば再利用
        if end_times and end_times[0] <= start:
            heapq.heappop(end_times)
        heapq.heappush(end_times, end)
    return len(end_times)


# テストコード
meetings = [[0, 30], [5, 10], [15, 20]]
print(min_meeting_rooms(meetings))  # 2