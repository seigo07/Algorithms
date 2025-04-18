
'''
プログラムの目的
与えられた昇順ソート済みの整数配列 nums に対して：
1.各要素を二乗する
2.二乗された値を昇順にソートして返す
'''


def sorted_squares(nums):
    n = len(nums)
    result = [0] * n  # 結果を格納する配列
    left, right = 0, n - 1  # left は先頭、right は末尾に配置
    pos = n - 1  # 後ろから埋める

    while left <= right:    # left と right の絶対値を比較し、大きい方の二乗値を後ろから順に詰める
        if abs(nums[left]) > abs(nums[right]):
            # 使ったポインタを内側に移動、posもデクリメント
            result[pos] = nums[left] ** 2
            left += 1
        else:
            # 使ったポインタを内側に移動、posもデクリメント
            result[pos] = nums[right] ** 2
            right -= 1
        pos -= 1

    return result

# 実行例
nums = [-7, -3, 0, 2, 5]
print(sorted_squares(nums))  # 出力: [0, 4, 9, 25, 49]
