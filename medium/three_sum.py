
# 配列 nums から、a + b + c = 0 となるindexが重複しない3つの数字の組み合わせをすべて探す
# 時間計算量: O(n²) 各 i に対して l, r を最大n回動かす
# 空間計算量: O(n) Pythonの sort() が最悪O(n)程度の補助領域を使用

# ソート + 2ポインタ(left, right)
def three_sum(nums):
    nums.sort()
    result = []
    # 3つの要素を選ぶので、i は最後から3番目まで
    # nums[i]：1つ目の数値
    # nums[left]：2つ目の数値(i + 1)
    # nums[right]：3つ目の数値(len(nums) - 1)
    for i in range(len(nums) - 2):
        # iが同じ前の数と同じならスキップして重複を防ぐ 
        # ex. nums = [-4, -1, -1, 0, 1, 2] で i = 2 のとき、nums[i] == nums[i - 1] # -1 == -1
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # left,right が同じ前の数と同じならスキップして重複を防ぐ 
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result


# 実行
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))