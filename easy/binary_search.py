# binarySearchを使用して与えられた配列numsからtargetを検索し、
# 見つかった場合はそのindexを返し、ない場合は-1を返す
# 配列の中央の要素と目標を比較し、目標が中央の要素よりも大きいか小さいかに応じて、
# 探索範囲を半分に狭めていく事で、O(log n)の時間複雑度で効率的に探索可能


def binary_search(nums, target):
    low = 0
    high = len(nums)-1
    while low < high:
        # リスト内の中央値のindexを取得
        mid = (low + high) // 2
        if nums[mid] == target:
            # targetが見つかった場合
            return mid
        elif nums[mid] < target:
            # ターゲットが中央より大きい場合、indexの下限をmid+1に設定し、探索を右側に絞る
            low = mid + 1
        else:
            # ターゲットが中央より大きい場合、indexの上限をmid-1に設定し、探索を左側に絞る
            high = mid - 1
    # targetが見つからない場合
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
index = binary_search(nums, target)
print(f"The target {target} is at index: {index}")


target = 2
index = binary_search(nums, target)
print(f"The target {target} is at index: {index}")
