
'''
nums の中から、2つの数を選んで足し合わせて、
target を達成する2つのindexを見つける
'''

# 配列を一度しか走査しないため、計算量が O(n)で済む
def two_sum(nums, target):

    # numとindexを記録
    num_dict = {}

    # 配列を走査し、indexとnumを取得
    for i, num in enumerate(nums):
        # 対象となるもう一つの値（補数）を計算
        complement = target - num
        # 補数がすでに辞書にあるかcheck
        if complement in num_dict:
            # 補数のindexと現在のindexを返すxのペアを返す
            return [num_dict[complement], i]

        # 走査されたiとnumを保存
        # e.g. [2: 0]
        # key: num
        # value: i
        num_dict[num] = i

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output will be [0, 1]
