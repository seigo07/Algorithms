
# すべての新鮮なオレンジ（1）が腐るまでの最短時間を求める
# 0は空のセル、1 は新鮮なオレンジ、2 は腐ったオレンジを表す

# 基本アルゴリズム: BFS

# 1. 初期化：腐ったオレンジ（2）をすべてキューに入れる。
# 2. 探索：キューから取り出し、上下左右の新鮮なオレンジを腐らせる。
# 3. 時間管理：1分ごとに腐るオレンジをまとめて処理する。
# 4. 終了判定：新鮮なオレンジが残っていれば -1、なければ経過時間を返す。
# ポイントは、最初から腐っているオレンジを同時に探索開始する

# 時間・空間計算量: O(mn) m 行、n 列のグリッド 空間はqueue計算量（それ以外はO(1)）

from collections import deque


def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    minutes = 0

    # ① 全セルを調べ、腐ったオレンジをキューへ
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                queue.append((r,c))

    # ② 上下左右の移動方向
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # ③ BFSで1分ずつ腐らせる
    while queue and fresh > 0:
        for _ in range(len(queue)):
            i,j = queue.popleft()
            for x,y in directions:
                ni,nj = i + x, j + y
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    queue.append((ni,nj))
        minutes += 1

    # ④ 新鮮なオレンジが残っているか判定
    return -1 if fresh > 0 else minutes


# 使用例
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(oranges_rotting(grid))  # 出力: 4

