# 面積 = 2本の間の距離 × 低い方の高さ が最大になる組み合わせを求める
# 時間計算量: O(n)
# 空間計算量: O(1)

# 現在の面積を計算(面積 = 2本の間の距離(right - left) × 低い方の高さ)
# max_area を更新
# 高さが低い側のポインタを内側へ移動
# left == right になるまで繰り返す
def max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        area = (right - left) * min(height[left],height[right])
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))  # 49