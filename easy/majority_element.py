
# 配列内で半数を超えて出現する数字を返す

# 基本アルゴリズム: Boyer-Moore投票法

# 1. 候補 candidate と票数 count を初期化
# 2. 配列を先頭から順番に確認
# 3. count が0なら現在の数字を候補にする
# 4. 候補と同じ数字なら count を+1
# 5. 異なる数字なら count を-1
# 6. 最後に候補を返す

# 時間計算量：O(n) 空間計算量：O(1)


def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


# テストコード
print(majority_element([3, 2, 3]))           # 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2

