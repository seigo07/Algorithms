# 整数配列の中に、同じ値が2回以上登場するかを判定
# 時間・空間計算量：O(n) 
def contains_duplicate(nums: list[int]) -> bool:
    # setは重複を保持しないため、要素数が減れば重複がある
    return len(nums) != len(set(nums))


print(contains_duplicate([1, 2, 3, 1]))              # True
print(contains_duplicate([1, 2, 3, 4]))              # False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2]))  # True