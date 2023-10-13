# 与えられた株価の配列から最大の利益を見つける
# 与えられた配列 prices は、各日の株価を表している
# この配列内で株を一度だけ買い、将来のある日にそれを売却して利益を最大化するのが目的


def max_profit(prices):
    # 最小価格を初期化
    min_price = float("inf")
    # 最大利益を初期化
    max_profit = 0

    for price in prices:
        if price < min_price:
            # より小さい価格が見つかったら最小価格を更新
            min_price = price
        else:
            # より大きな利益が見つかったら最大利益を更新
            max_profit = max(max_profit, price - min_price)


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
