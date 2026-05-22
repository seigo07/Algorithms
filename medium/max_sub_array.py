# 整数配列から、連続する部分配列の最大合計を求める
# Kadaneアルゴリズム: 各要素で「前の合計に足す」か「ここから新しく始める」かを選び、最大値を更新
# 時間計算量: O(n)
# 空間計算量: O(1)
def max_sub_array(nums):

    # 現在位置までの「最大部分配列和」 全体で見つかった最大値
    current_sum = max_sum = nums[0]

    for num in nums[1:]:

        # 前の部分配列に足すか、ここから新しく始めるか
        current_sum = max(num, current_sum + num)

        # 最大値を更新
        max_sum = max(max_sum, current_sum)

    return max_sum

nums = [1, -3, 4, -1, 2, 1, -5, 3]
print(max_sub_array(nums))
