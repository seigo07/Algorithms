# 動的計画法を使用し、1回に 1段 or 2段 登れるとき、n段の階段を何通りで登れるかを求める
# dp[n] = dp[n-1] + dp[n-2]
# 時間計算量: O(n) 空間計算量: O(1) 変数3個だけ
def climb_stairs(n):
    # 1・2はそのまま返す 1段なら1通り、2段なら2通り
    if n <= 2:
        return n
    
    # prev2 = dp[i-2], prev1 = dp[i-1]
    prev2, prev1 = 1, 2

    # 動的計画法（フィボナッチ数列）を使用してステップ数を計算（最初の2つの数が1で、それ以降の数は前の2つの数の和である数列）
    # n = 10 -> [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # 3段目からn段目まで計算
    for i in range(3, n + 1):
        curr = prev2 + prev1
        prev2 = prev1
        prev1 = curr
    
    return curr # dpの最後が最終ステップ数


# n = 4
print(climb_stairs(4))  # 5
