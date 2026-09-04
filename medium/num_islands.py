# 「1」(陸地) と「0」(水)
# 「まだ見てない1」を見つけたらcount+1 
# 「上下左右の1」をDFS/BFSで再帰探索
# 見つけた陸は "0" に変更し訪問済みにする
# 時間・空間計算量: O(mn)

from collections import deque

def num_islands(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # スタック（LIFO）/ 再帰関数 / 組み合わせ全列挙
    def dfs(r, c):
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
        
            grid[r][c] = '0'  # 訪問済みにする

            # 上下左右探索
            dfs(r - 1, c)    # 上
            dfs(r + 1, c)    # 下
            dfs(r, c - 1)    # 左
            dfs(r, c + 1)    # 右


    # queueに入れ、1個ずつ取り出して上下左右を見る(+1の上下左右のマスを見る。次に+2の上下左右のマスを見る。次に+3の上下左右のマスを見る)
    # キュー（FIFO）/ 最短経路
    def bfs(r, c):
        q = deque([(r, c)])
        grid[r][c] = "0"  # 訪問済み

        while q:
            r, c = q.popleft()  # 「1」(陸地)の座標を一個ずつ取り出す

            # 上下左右探索
            for nr, nc in [
                (r - 1, c),  # 上
                (r + 1, c),  # 下
                (r, c - 1),  # 左
                (r, c + 1)   # 右
            ]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"  # 訪問済みにする
                    q.append((nr, nc))  # 「1」(陸地)の座標を追加

    # 左上から全マスを確認し、上下左右のそれぞれ行き止まり(1→0)まで探す
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':   # 新しい島発見
                count += 1
                # dfs(r, c)
                bfs(r, c)

    return count


grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

print(num_islands(grid)) # 出力: 3 (左上、真ん中、右下)