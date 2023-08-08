# 整数配列 nums を指定して、サブアレイ 最大の合計を求め、その合計を返します。

# このプログラムは、与えられた整数のリスト nums から最大の連続した部分列の合計を求める問題を解くものです。(Kadaneのアルゴリズム)
class Solution(object):
    def maxSubArray(self, nums):
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current
        return max_global


# インスタンスの作成
solution = Solution()

nums = [1, -3, 4, -1, 2, 1, -5, 3]
print(solution.maxSubArray(nums))
