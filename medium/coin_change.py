# 動的計画法を用いて合計金額を作るための最小コイン枚数を求める
# 作れない場合は -1 を返す
# 時間計算量: O(amount × len(coins)) 空間計算量: O(amount)
def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)  # 到達不可な最大値で初期化
    dp[0] = 0  # 初期条件: 0円を作るのに必要なコイン枚数は0枚 n = 11 → [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]

    # 1円〜amountまで順番に計算
    for i in range(1, amount + 1):
        # 各コインを試す
        for coin in coins:
            # コインが使える場合
            if i - coin >= 0:
                # 最小枚数を更新
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1


# 使用例
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # 出力: 3 (5 + 5 + 1 = 11 なので、3枚のコインが必要)
