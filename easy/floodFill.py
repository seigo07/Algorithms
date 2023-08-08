def floodFill(image, sr, sc, newColor):
    startColor = image[sr][sc]
    if startColor == newColor:
        return image
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    stack = [(sr, sc)]

    while stack:
        r, c = stack.pop()
        if image[r][c] == startColor:
            image[r][c] = newColor
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == startColor:
                    stack.append((nr, nc))

    return image


# 初期の画像を定義します。
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# 開始ピクセルは (1, 1) で、新しい色は 2 にします。
sr, sc, newColor = 1, 1, 2

# floodFill 関数を呼び出します。
newImage = floodFill(image, sr, sc, newColor)

# 新しい画像を出力します。
print(newImage)
