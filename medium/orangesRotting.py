# m x n のグリッドが与えられ、各セルには次の 3 つの値のいずれかを指定できます。
# 0は空のセルを表し、1 は新鮮なオレンジを表します、または2 腐ったオレンジを表します。
# 腐ったオレンジに 4 方向に隣接する新鮮なオレンジは 1 分ごとに腐っていきます。
# セルに新しいオレンジ色がなくなるまでに経過しなければならない最小時間を分単位で返します。それが不可能な場合は、-1 を返します。
from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0

        # すべての腐ったオレンジの位置と新しいオレンジの数をカウントします
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        # すべてのオレンジが腐っているか、もともとオレンジがない場合
        if not queue and not fresh_oranges:
            return 0

        minutes = -1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                # 4方向に隣接するセルを確認します
                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + x, j + y

                    # 新しいオレンジがある場合、それを腐らせてキューに追加します
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh_oranges -= 1
                        queue.append((ni, nj))

            minutes += 1

        # すべてのオレンジが腐っているかを確認します
        if fresh_oranges == 0:
            return minutes
        else:
            return -1


# インスタンスの作成
solution = Solution()

# 使用例
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(solution.orangesRotting(grid))  # 出力: 4

