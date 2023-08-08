# 整数配列 nums を指定すると、i != j、i != k、j != k、および nums[i] + となるすべてのトリプレット [nums[i], nums[j], nums[k]] を返します。 nums[j] + nums[k] == 0。

# このプログラムは、整数の配列 nums から、合計が0になる3つの数の組を探します。
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result, visited = [], set()

        for i in range(len(nums)):
            if nums[i] > 0:  # 三つの数の合計が0になるため、最小の数が正の場合、以降の数を探索する必要はありません
                break
            if i == 0 or nums[i] != nums[i - 1]:  # 同じ数を二度探索しないためのチェック
                self.twoSum(nums, i, result)

        return result

    def twoSum(self, nums, i, result):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                result.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:  # 重複を避ける
                    j += 1
            seen.add(nums[j])
            j += 1


# インスタンスの作成
solution = Solution()

# 使用例:
nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))
