# Given an m x n 2D binary grid grid which represents
# a map of '1's (land) and '0's (water), return the number of islands.

# 「1」(陸地) と「0」(水) の地図を表す m x n 2D バイナリ グリッドを指定すると、島の数を返します。
# 与えられた2Dバイナリグリッドで島の数をカウントするPythonプログラムです。
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # マークする
            dfs(i - 1, j)    # 上
            dfs(i + 1, j)    # 下
            dfs(i, j - 1)    # 左
            dfs(i, j + 1)    # 右

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count


# インスタンスの作成
solution = Solution()

# 使用例
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(solution.numIslands(grid))  # 出力: 3
