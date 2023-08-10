# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# 重複しない間隔の配列が与えられます。
# interval[i] = [starti, endi] は i 番目の間隔の開始と終了を表し、間隔は starti によって昇順に並べ替えられます。
# また、別の間隔の開始と終了を表す間隔 newInterval = [start, end] も指定されます。
# newInterval を間隔に挿入して、間隔が starti によって昇順にソートされ、間隔に重複する間隔が存在しないようにします (必要に応じて重複する間隔をマージします)。
# 挿入後の間隔を返します。

# このプログラムは、与えられた間隔のリストに新しい間隔を挿入し、必要に応じて重複する間隔をマージする機能を提供します。
class Solution(object):
    def insert(self, intervals, newInterval):
        # 結果を格納するためのリスト
        result = []
        # 新しいインターバル
        start, end = newInterval

        for i, (s, e) in enumerate(intervals):
            # 新しいインターバルが現在のインターバルよりも後ろにある場合
            if end < s:
                i -= 1
                break
            # 新しいインターバルが現在のインターバルと重複している場合
            elif start <= e:
                start = min(start, s)
                end = max(end, e)
            else:
                result.append([s, e])

        return result + [[start, end]] + intervals[i+1:]


# インスタンスの作成
solution = Solution()

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(solution.insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(solution.insert(intervals, newInterval))
