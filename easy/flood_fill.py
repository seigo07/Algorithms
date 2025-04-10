'''
DFSを使用して、
指定された座標 (sr, sc) から始めて、
同じ色の隣接ピクセルをすべて指定された新しい color に塗り替える

'''

# sr, sc: 開始位置
def flood_fill(image, sr, sc, newColor):

    """
    :param sr: 塗りつぶしを開始する座標の行インデックス。
    :param sc: 塗りつぶしを開始する座標の列インデックス。
    :param newColor: 新しい色の整数値。指定された座標から始まる領域内のすべてのピクセルがこの色に変更される。
    """

    # 初期位置の色（塗りつぶしを開始する色）を取得
    startColor = image[sr][sc]

    # すでに同じ色なら何もしない
    if startColor == newColor:
        return image

    # DFSは再帰的なアルゴリズムであり、木やグラフ構造など、非線形なデータの探索に適している
    # 指定された座標 (r, c) から連結した領域（下、上、右、左）を再帰的に探索し塗りつぶす
    def dfs(r, c):

        # (r, c)がindexを超えず、
        # image[r][c]の色が startColor である場合にのみ処理を実行
        if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == startColor:

            # 現在のピクセルを newColor に変更
            image[r][c] = newColor

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
newImage = flood_fill(image, 1, 1, 2)

# 結果の表示
for row in newImage:
    print(row)
