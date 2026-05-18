# DFSを使用して、指定された座標 (r, c) から連結した領域（下、上、右、左）を再帰的に探索し塗りつぶす
# 時間・空間計算量: O(mn) m = 行数, n = 列数 最悪全マス見る キューに最大で全マス近く入る可能性がある
def flood_fill(image, sr, sc, new_color):

    """
    :param sr: 塗りつぶしを開始する座標の行インデックス。
    :param sc: 塗りつぶしを開始する座標の列インデックス。
    :param new_color: 新しい色の整数値。指定された座標から始まる領域内のすべてのピクセルがこの色に変更される。
    """

    # 塗りつぶしを開始する位置の色を取得
    start_color = image[sr][sc]

    # すでに指定された色に塗りつぶされている場合は何もしない
    if start_color == new_color:
        return image

    # 指定された座標 (r, c) から連結した領域（下、上、右、左）を再帰的に探索し塗りつぶす
    def dfs(r, c):

        # (r, c)がindexを超えず、image[r][c]の色が start_color である場合にのみ処理を実行
        if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == start_color:

            # 現在のピクセルを new_color に変更
            image[r][c] = new_color

            # 4方向（下、上、右、左）に対して再帰的に dfs を呼び出す
            # 同じ色で連結した領域がすべて新しい色に変更される
            dfs(r + 1, c) # 下
            dfs(r - 1, c) # 上
            dfs(r, c + 1) # 右
            dfs(r, c - 1) # 左

    # 深さ優先探索を開始
    dfs(sr, sc)

    return image


# サンプル画像
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

# 画像を塗りつぶし
new_image = flood_fill(image, 1, 1, 2)

# 結果の表示
for row in new_image:
    print(row)
