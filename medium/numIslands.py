# 「1」(陸地) と「0」(水)
# 「まだ見てない1」を見つけたら、上下左右をDFS/BFSで再帰探索
#  カウント+1（探索済みとする）

from collections import deque

def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # 上下左右のそれぞれ行き止まり(1→0)まで探す
    # 行き止まったら次へ行く(上→下→左→右)
    # スタック（LIFO）/ 再帰関数 / 組み合わせ全列挙
    def dfs(r, c):
        if (
            r < 0 or r >= rows or   # 範囲外
            c < 0 or c >= cols or   # 海
            grid[r][c] == "0"       # 訪問済み
        ):
            return
        
        grid[r][c] = '0'  # 訪問済みにする

        # 上下左右探索
        dfs(r - 1, c)    # 上
        dfs(r + 1, c)    # 下
        dfs(r, c - 1)    # 左
        dfs(r, c + 1)    # 右

    # 1見つけたらqueueに入れる
    # 1個ずつ取り出して上下左右を見る(+1の上下左右のマスを見る。次に+2の上下左右のマスを見る。次に+3の上下左右のマスを見る)
    # キュー（FIFO）/ 最短経路
    def bfs(r, c):
        q = deque([(r,c)])  # 最初の島セルを入れる
        grid[r][c] = '0'  # 訪問済みにする

        # queueが空になるまで探索
        while q:
            r, c = q.popleft()  # 先頭取り出し

            # 上下左右
            directions = [
                (-1, 0),  # 上
                (1, 0),   # 下
                (0, -1),  # 左
                (0, 1)    # 右
            ]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # 範囲内 かつ 島なら
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == "1"
                ):
                    grid[nr][nc] = "0"  # 訪問済みにする
                    q.append((nr, nc))  # 次に探索するためqueueへ

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':   # 新しい島発見
                # dfs(r, c)
                bfs(r, c)
                count += 1

    return count

grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

print(numIslands(grid)) # 出力: 3 (左上、真ん中、右下)