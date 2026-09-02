# 配列 nums から、a + b + c = 0 となる重複しない3つの数字の組み合わせをすべて探す
# 時間計算量: O(n²) 各 i に対して l, r を最大n回動かす
# 空間計算量: O(n) Pythonの sort() が最悪O(n)程度の補助領域を使用

# ソート + 2ポインタ(left, right)
def three_sum(nums):
    nums.sort()
    ans = []
    # 3つの要素を選ぶので、i は最後から3番目まで
    for i in range(len(nums) - 2):
        # iが同じ前の数と同じならスキップして重複を防ぐ 
        # ex. nums = [-4, -1, -1, 0, 1, 2] で i = 2 のとき、nums[i] == nums[i - 1] # -1 == -1
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # l,r が同じ前の数と同じならスキップして重複を防ぐ 
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
    return ans


# 実行
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))