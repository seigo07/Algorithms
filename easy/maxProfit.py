# 一番安い日に買って、その後の一番高い日に売ると利益が最大になる
# 時間計算量: O(n)
# 空間計算量（メモリ）: O(1)
def max_profit(prices):
    
    min_price = float("inf")    # 最初のループで値を最小値として保持するため、無限大の値を設定
    max_profit = 0    # 最初の最大利益は0

    for price in prices:
        min_price = min(min_price, price)   # より小さい価格が見つかったら最安値を更新
        profit = price - min_price   # 今日売った場合の利益
        max_profit = max(max_profit, profit)    # より大きな利益が見つかったら最大利益を更新

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
