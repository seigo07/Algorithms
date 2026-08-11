# 整数配列の非ゼロ要素の順序を維持したまま、すべての0を末尾へ移動
# 時間計算量：O(n) 空間計算量：O(1)

def move_zeroes(nums):
    write = 0  # 次の非ゼロ要素を置く位置

    for read in range(len(nums)):  # len(nums)までのindexを走査 ex. 0,1,2,3,4
        # 現在要素が非ゼロかチェック
        if nums[read] != 0:
            # 非ゼロ要素とwrite位置の要素を交換
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)  # [1, 3, 12, 0, 0]