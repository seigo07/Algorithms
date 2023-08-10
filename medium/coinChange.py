# You are given an integer array coins representing coins of different denominations
# and an integer amount representing a total amount of money.

# この問題は「コイン変更問題」として知られており、動的計画法（特に1次元DP配列を使用するアプローチ）を用いて解く

# このプログラムは、指定された額を作るために必要な最小のコイン数を計算するものです。
# coinChange関数は、コインの種類と額を引数として受け取り、必要な最小のコイン数を返します。
class Solution(object):
    def coinChange(self, coins, amount):
        # DP 配列の初期化: とても大きな値で初期化して、min関数を使いやすくする
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 初期条件: 0円を作るのに必要なコインは0枚

        # DP 過程
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


# インスタンスの作成
solution = Solution()

# 使用例
coins = [1, 2, 5]
amount = 11
print(solution.coinChange(coins, amount))  # 出力: 3 (5 + 5 + 1 = 11 なので、3枚のコインが必要)
