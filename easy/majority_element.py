
# 配列 nums の中で多数派要素（出現回数が n // 2 より多い要素）を見つける

def majority_element(nums):
    # カウントと現在の候補
    count = 0
    candidate = None

    for num in nums:
        # カウントがゼロになったら新しい候補に切り替え
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)  # 同じなら+1、違えば-1

    return candidate # 最後に残った候補が多数派要素

nums = [2, 2, 1, 1, 1, 2, 2]
print("多数派要素:", majority_element(nums))
