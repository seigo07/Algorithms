# 「隣り合う家は同時に選べない」というルールの中で、合計金額が最大になる家の組み合わせを探す（DPを使う）
# 時間計算量: O(n) 空間計算量: O(1)
def rob(nums):
    # 2つ前までの最大金額
    prev2 = 0

    # 1つ前までの最大金額
    prev1 = 0

    for money in nums:
        # 今の家を盗まない場合: prev1
        # 今の家を盗む場合: prev2 + money
        current = max(prev1, prev2 + money)

        prev2 = prev1
        prev1 = current

    return prev1


nums = [1, 2, 3, 1]
print(rob(nums))  # 4
