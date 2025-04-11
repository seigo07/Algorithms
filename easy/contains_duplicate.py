
'''

整数配列 nums において、重複する値が存在するかどうかを判定し、
重複があれば True
全て異なれば False
を返す。

'''


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True  # 重複発見
        seen.add(num)
    return False  # 重複なし

# 実行例
print(contains_duplicate([1, 2, 3, 4]))      # False
print(contains_duplicate([1, 2, 3, 1]))      # True
