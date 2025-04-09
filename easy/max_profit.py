
'''
与えられた株価の配列から最大の利益を見つける
与えられた配列 prices は、各日の株価を表している
この配列内で株を一度だけ買い、将来のある日にそれを売却して利益を最大化するのが目的
'''


def max_profit(prices):

    min_price = float("inf")  # 最初のループで値を最小値として保持するため、無限大の値を設定
    max_profit = 0  # 最初の最大利益は0

    for price in prices:
        if price < min_price:
            # より小さい価格が見つかったら最小価格を更新
            min_price = price
        elif price - min_price > max_profit:
            # より大きな利益が見つかったら最大利益を更新
            max_profit = price - min_price
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
