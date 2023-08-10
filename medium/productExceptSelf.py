# Given an integer array nums, return an array answer such that
# answer[i] is equal to the product of all the elements of nums except nums[i].

# 指定された位置の要素を除く、配列内のすべての要素の積を求める
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)

        # 左から右への積を格納する配列
        left_products = [1] * n
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # 右から左への積を格納する配列
        right_product = 1
        for i in range(n - 1, -1, -1):
            left_products[i] = left_products[i] * right_product
            right_product *= nums[i]

        return left_products


# インスタンスの作成
solution = Solution()

# 使用例
nums = [1, 2, 3, 4]
print(solution.productExceptSelf(nums))  # [24, 12, 8, 6]
