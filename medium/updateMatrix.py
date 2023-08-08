from collections import deque

# m x n のバイナリ行列マットを指定すると、各セルの最も近い 0 の距離を返します。
# 隣接する 2 つのセル間の距離は 1 です。

# このプログラムは、与えられた m x n のバイナリ行列内で各セルから最も近い0のセルまでの距離を計算して返します。(幅優先探索(BFS))
class Solution(object):
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        dist = [[float('inf')]*n for _ in range(m)]
        queue = deque([])

        # Initialize queue with all 0's positions
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))  # put all 0s in the queue.

        # 4 directions: up, down, left, right
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y = queue.popleft()  # pop the cell from the queue
            for dx, dy in dirs:  # iterate over all directions
                nx, ny = x + dx, y + dy  # next cell in the current direction
                # If the next cell is within the grid and is closer when reached from the current cell
                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1  # update the distance of the next cell
                    queue.append((nx, ny))  # append the next cell into the queue

        return dist


# インスタンスの作成
solution = Solution()

# 上記で定義したupdateMatrix関数を使用
mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]

result = solution.updateMatrix(mat)
for row in result:
    print(row)
