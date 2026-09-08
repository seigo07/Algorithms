# 合計が k になる連続した部分配列の個数を求める
# 時間・空間計算量: O(n)

# prefix に現在までの累積和を入れる
# prefix - k (過去の累積和) の回数を count に追加
# freq に 過去のprefixとその出現回数 を保存

def subarray_sum(nums, k):
    prefix = 0          # 現在までの累積和
    count = 0           # 条件を満たす部分配列の数
    freq = {0: 1}       # 過去の累積和 → 出現回数

    for num in nums:
        prefix += num

        # prefix - 過去の累積和 = k → 過去の累積和 = prefix - k 
        # prefix - kが過去に出現してなければ 0 を返す
        count += freq.get(prefix - k, 0)

        # 現在の累積和を記録
        freq[prefix] = freq.get(prefix, 0) + 1

    return count


nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))  # 2