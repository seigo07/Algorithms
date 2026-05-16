# 二分探索によりソート済み配列から目的の値を高速に探す
# 見つかった場合はそのindexを返し、ない場合は-1を返す
# 時間計算量: O(log n)　配列の中央の要素と目標を比較し大きいか小さいにより探索範囲をどちらか半分に狭める
# 空間計算量: O(1)
def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        # リスト内の中央値のindexを取得
        mid = (left + right) // 2
        # targetが中央値
        if nums[mid] == target:
            return mid
        # ターゲットが中央より大きい場合、indexの下限をmid+1に設定し、探索を右側に絞る
        elif nums[mid] < target:
            left = mid + 1
        # ターゲットが中央より大きい場合、indexの上限をmid-1に設定し、探索を左側に絞る
        else:
            right = mid - 1
    # targetが見つからない場合
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
index = binary_search(nums, target)
print(f"The target {target} is at index: {index}")


target = 2
index = binary_search(nums, target)
print(f"The target {target} is at index: {index}")
