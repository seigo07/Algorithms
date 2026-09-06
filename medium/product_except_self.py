# 各要素について、自分自身を除いた全要素の積を求める
# 時間計算量: O(n)
# 空間計算量: O(1)
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # 各iの左側の積をanswerに保存 ex. [1, 1, 2, 6]
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # 各iの右側の積をanswerに掛ける ex. [24, 12, 4, 1]
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


nums = [1, 2, 3, 4]
print(product_except_self(nums))
# [24, 12, 8, 6] ([1, 1, 2, 6] * [24, 12, 4, 1])
