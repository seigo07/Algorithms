# 整数配列から、連続する部分配列の最大合計を求める
# Kadaneアルゴリズム: 配列を左から走査し、各要素で「前の合計に足す」か「ここから新しく始める」かを選び、最大値を更新
# 時間計算量: O(n)
# 空間計算量: O(1)
def max_sub_array(nums):

    current_sum = max_sum = nums[0]  # 現在位置で終わる最大合計

    # rangeを使用する事で空間計算量がo(1)になる
    for i in range(1, len(nums)):
        num = nums[i]

        # 「前の合計に足す」か「ここから新しく始める」かを比較
        current_sum = max(num, current_sum + num)

        # 全体の最大値を更新
        max_sum = max(max_sum, current_sum)

    return max_sum

nums = [1, -3, 4, -1, 2, 1, -5, 3]
print(max_sub_array(nums))
