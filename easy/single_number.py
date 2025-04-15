
'''

整数配列 nums において、すべての要素が2回ずつ出現するが、1つだけ1回しか出現しない要素を求める

時間計算量：O(n)
空間計算量：O(1)

アルゴリズム概要（XORを使用）
XOR（排他的論理和）の性質を使う：

a ^ a = 0（同じ数をXORすると0になる）
a ^ 0 = a

XORは交換法則・結合法則が成り立つ
したがって、すべての要素をXORすれば、2回出てくる要素は消え、1回だけ出現する要素だけが残る

'''


def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


# 実行例
nums = [4, 1, 2, 1, 2]
print(single_number(nums))  # 出力: 4
