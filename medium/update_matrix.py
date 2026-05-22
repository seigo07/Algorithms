# 各セルについて、最も近い 0 までの距離を求める
# すべての 0 を始点にして BFS する
# 0 から同時に広がることで、各 1 に最短距離が入る
# 時間計算量: O(m * n) 各セルを最大1回だけ処理する
# 空間計算量: O(m * n) dist とキューで最大 m * n 使う
from collections import deque

def update_matrix(mat):
    rows, cols = len(mat), len(mat[0])
    # 各セルから一番近い 0 までの距離 [[-1, -1, -1],[-1, -1, -1],[-1, -1, -1]]
    dist = [[-1] * cols for _ in range(rows)]
    # BFSで次に調べるセルを入れる
    queue = deque()

    # すべての 0 を BFS の開始点にする
    # dist [[0, 0, 0],[0, -1, 0],[-1, -1, -1]]
    # queue ([(0,0), (0,1), (0,2), (1,0), (1,2)])
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))

    # 下, 上, 右, 左
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 複数始点 BFS
    while queue:
        r, c = queue.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            # 未訪問のセルだけ更新
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                # 今いるセル (r,c) の距離に 1 足して、隣のセルの距離を決める
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return dist


mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
]

result = update_matrix(mat)
for row in result:
    print(row)
