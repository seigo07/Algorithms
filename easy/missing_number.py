# 0からnまでの整数のうち、配列numsに存在しない数字を1つ見つける
# 時間計算量：O(n) 空間計算量：O(1)

def missing_number(nums):
    n = len(nums)                  # 配列の要素数。数字の範囲は 0～n
    missing = n * (n + 1) // 2     # 0～n の合計値

    # 配列内の数字を合計値から引く
    for num in nums:
        missing -= num

    return missing                 # 最後に残った値が欠けている数字


# 実行例
nums = [3, 0, 1]
print(missing_number(nums))  # 2