
'''
配列 nums に対して、すべての0を末尾に移動し、0でない要素の相対順序を保つ
追加の配列を使わず（in-place）に実行する
'''


def move_zeroes(nums):
    non_zero_index = 0  # 0でない要素を挿入する位置

    # ステップ1: 非ゼロ要素を前に詰める
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1

    # ステップ2: 残りの位置を0で埋める
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0


nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)  # 出力: [1, 3, 12, 0, 0]
