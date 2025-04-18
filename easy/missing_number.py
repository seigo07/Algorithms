
'''
配列 nums（0～n のうち n 個の異なる数が含まれている）から、1つだけ存在しない数を見つけること。
'''


def missing_number(nums):
    n = len(nums) # 配列の長さ
    expected_sum = n * (n + 1) // 2  # 0 から n までの合計（ガウスの公式）
    actual_sum = sum(nums)          # 配列 nums に含まれる数の実際の合計を計算
    return expected_sum - actual_sum    # 欠けている数 = 理論上の合計 − 実際の合計


# 実行例
nums = [3, 0, 1]
print(missing_number(nums))  # 出力: 2
