# ある数列が与えられたときにその数列内で目的の数字(target)の位置を返す必要があります。
# 数列は元々昇順にソートされていたが、ある点でローテーションされる可能性があります。
# このローテーションは任意の位置で行われるため、数列内の数の順番は変わっている可能性があります。
class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            # この部分が通常のバイナリサーチと異なります。
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


# インスタンスの作成
solution = Solution()

# 使用例
nums = [4,5,6,7,0,1,2]
target = 0
print(solution.search(nums, target))  # 4が出力される

target = 3
print(solution.search(nums, target))  # -1が出力される
