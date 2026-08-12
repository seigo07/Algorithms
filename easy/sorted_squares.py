# 昇順に並んだ整数配列の各要素を2乗し、その結果を昇順で返す
# 時間計算量：O(n log n)2乗処理は O(n)、並べ替えは O(n log n)
# 空間計算量：O(n)

def sorted_squares(nums):
    # 各要素を2乗し、小さい順に並べる
    return sorted(x * x for x in nums)


# 実行例
nums = [-4, -1, 0, 3, 10]
result = sorted_squares(nums)
print(result)  # [0, 1, 9, 16, 100]