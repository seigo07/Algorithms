# 配列 nums の中から足して target になる 2つの数字の index を返す。
def two_sum(nums, target):

    num_dict = {}   # ループした{num: i}を保存

    # 1回ループするだけなので計算量が O(n)で済む
    for i, num in enumerate(nums):
        complement = target - num   # 残りの必要な値を計算

        # 必要な値が既にあれば答え
        if complement in num_dict:
            return [num_dict[complement], i]

        # 必要な値がなければ今の値とiを保存
        num_dict[num] = i
    return None


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  #[0, 1]
