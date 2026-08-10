# 整数配列で、ほかの値がすべて2回ずつ現れる中、1回だけ現れる値を求める
# 時間計算量: O(n) 空間計算量: O(1)

def single_number(nums):
    result = 0

    # 全要素をXOR（排他的論理和）する
    for num in nums:
        result ^= num # 重複要素は入らない

    return result


# 実行例
nums = [2, 2, 1]
print(single_number(nums))  # 1