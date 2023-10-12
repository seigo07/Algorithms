# 配列 nums の中から、2つの数を選んで足し合わせて、
# 目標値 target を達成するような2つの数のインデックスを見つける


# 配列を一度しか走査しないため、計算量が O(n)で済む
def two_sum(nums, target):

    # ループしたnum, iを保存するためのdict
    num_dict = {}

    # 配列を一度走査し、check if target - num in num_dict
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            # 差が辞書に存在する場合、辞書の差がkeyのindexと現在のindexのペアを返す
            return [num_dict[complement], i]

        # 走査されたiとnumを保存
        # e.g. [2: 0]
        # key: num
        # value: i
        num_dict[num] = i
    return None


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output will be [0, 1]
