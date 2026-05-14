# 配列numsの中から足してtargetになる2つのindexを返す
def two_sum(nums, target):

    seen = {}   # ループした{num: i}を保存

    # 1回ループするだけなので計算量が O(n)で済む
    for i, num in enumerate(nums):
        complement = target - num   # 残りの必要な値を計算

        # 必要な値が既にあれば答え
        if complement in seen:
            return [seen[complement], i]

        # 必要な値がなければ今の値とiを保存
        seen[num] = i
    return None


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  #[0, 1]
