
# 回転された昇順配列 nums から target を探し、存在すればそのインデックス、存在しなければ -1 を返す
# 回転されていても、中央で分割した左右の少なくとも一方は昇順になっている

# 基本アルゴリズム: Binary Search

# 1. left と right で探索範囲を決める。
# 2. mid（中央のインデックス）を計算する。
# 3. nums[mid] == target なら mid を返す。
# 4. 左半分と右半分のどちらが昇順かを判定する。
# 5. target が存在し得る側だけを残して探索範囲を狭める。
# 6. 見つからなければ -1 を返す。

# 時間計算量：O(log n) 空間計算量：O(1)


def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # 左半分が昇順の場合
        if nums[left] <= nums[mid]:
            # target が左半分にあるなら左を探索
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            # target が右半分にあるなら右を探索
            else:
                left = mid + 1
        # 右半分が昇順の場合
        else:
            # target が左半分にあるなら左を探索
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            # target が左半分にあるなら左を探索
            else:
                right = mid - 1
    return -1


# 使用例
nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))  # 4が出力される

target = 3
print(search(nums, target))  # -1が出力される
