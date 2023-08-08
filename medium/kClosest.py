# Points[i] = [xi, yi] が X-Y 平面上の点を表す点の配列と整数 k を指定すると、原点 (0, 0) に最も近い k 個の点を返します。
# X-Y 平面上の 2 点間の距離はユークリッド距離 (つまり、√(x1 - x2)2 + (y1 - y2)2) です。
# 回答は任意の順序で返すことができます。
# 答えは一意であることが保証されます (順序を除く)。
# 定義した関数
import heapq

# このプログラムは、2D平面上の点群の中から、原点 (0, 0) に最も近いk個の点を返す関数 kClosest を定義しています。
class Solution(object):
    def kClosest(self, points, k):
        def distance(point):
            return point[0]**2 + point[1]**2
        return heapq.nsmallest(k, points, key=distance)

# インスタンスの作成
solution = Solution()

# 使用例
points = [[1,3],[-2,2],[2,-2],[4,5],[-1,-1]]
k = 3

result = solution.kClosest(points, k)
print(result)  # Expected output: [[-2,2],[1,3],[2,-2]] またはこの要素の異なる順序
