# 動的計画法を使用し、階段を登る方法の数を計算
# 毎回1ステップまたは2ステップを進むことができる


def climb_stairs(n):
    # n = 1の場合、一歩の1パターン
    # n = 2の場合、一歩ずつか二歩の2パターン
    if n <= 2:
        return n

    # 初期のステップ数を0をn個分に設定
    # e.g. n = 5 の場合 -> [0, 0, 0, 0, 0]
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    # 動的計画法（フィボナッチ数列）を使用してステップ数を計算
    # フィボナッチ数列は、最初の2つの数が1で、それ以降の数は前の2つの数の和である数列
    # e.g. n = 10の場合 -> [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in range(3, n + 1):
        # 前2つの数の和を dp[i] に登録
        dp[i] = dp[i - 1] + dp[i - 2]

    # dpの最後が最終ステップ数
    return dp[n]


# 例: n = 4
print(climb_stairs(10))  # 結果は5