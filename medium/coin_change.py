
# 指定された金額を作るために必要なコインの最小枚数を求める(DP)

# - 各コインは何度でも使用可能
# - 金額を作れなければ -1
# - amount = 0 なら 0

# 処理フロー
# 1. dp という配列を作成する。
# 2. dp[i] は「金額 i を作るための最小コイン枚数」を表す。
# 3. dp[0] = 0 に初期化する。
# 4. 金額 1 から amount まで順番に処理する。
# 5. 各金額について、使用できるコインを試し、最小枚数を更新する。
# 6. 最終的に dp[amount] を返す。作れなければ -1。

# 時間計算量: O(amount × len(coins)) 空間計算量: O(amount)


def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)  # 到達不可な最大値で初期化
    dp[0] = 0  # 初期条件: 0円を作るのに必要なコイン枚数は0枚 n = 11 → [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]

    # 1円〜amountまで順番に計算
    for i in range(1, amount + 1):
        # 各コインを試す
        for coin in coins:
            # コインが使える場合
            if coin <= i:
                # コインを1枚追加したとき、今までより少ない枚数で金額 i を作れるか比較し、最小枚数を更新
                # ex. coins = [1, 2, 5] amount = 11 → dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # amount + 1 は、全て1円コインの場合の amount 枚よりも大きい値なので、最小枚数としてあり得ない
    return dp[amount] if dp[amount] != amount + 1 else -1


# 使用例
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # 出力: 3 (5 + 5 + 1 = 11 なので、3枚のコインが必要)
