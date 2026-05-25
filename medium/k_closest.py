# points の中から、原点 (0,0) に近い点を（距離の2乗 = x² + y² の近い順に）k 個返す
# 時間計算量: O(n log n) 空間計算量: O(n) n は points の数
import heapq

def k_closest(points, k):
    # 各点と原点(0,0)との距離の2乗を計算
    def distance(point):
        return point[0]**2 + point[1]**2
    # distance が小さい順に k 個の点を取り出す
    return heapq.nsmallest(k, points, key=distance)


# 使用例
points = [[1,3],[-2,2],[2,-2],[4,5],[-1,-1]]
k = 3

result = k_closest(points, k)
print(result)  # Expected output: [[-2,2],[1,3],[2,-2]] またはこの要素の異なる順序
