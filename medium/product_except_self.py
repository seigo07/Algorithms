
# 各要素について、自分自身を除いた全要素の積を求める
# 基本アルゴリズム：Prefix Product（前方累積積）＋ Suffix Product（後方累積積）

# 処理フロー：
# 1. 左から順番に、自分より左側の積を記録
# 2. 右から順番に、自分より右側の積を掛ける
# 3. 完成した answer を返す

# 時間計算量: O(n)
# 空間計算量: answer以外の変数 O(1) answerは O(n)

def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # 各iの左側の積をanswerに保存 ex. [1, 1, 2, 6]
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # 各iの右側の積をanswerに掛ける ex. [24, 12, 4, 1]
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


nums = [1, 2, 3, 4]
print(product_except_self(nums))
# [24, 12, 8, 6] ([1, 1, 2, 6] * [24, 12, 4, 1])
