# 1〜n のバージョンの中で、最初に壊れたバージョンを探す
# 時間計算量: O(log n) 二分探索を使用する
# 空間計算量: O(1)
def first_bad_version(n):
    left, right = 1, n

    while left < right:

        # 中間値を計算
        mid = left + (right - left) // 2
        print(mid)
        
        if is_bad_version(mid):
            # 中間バージョンがバッドバージョンの場合、左半分に絞る e.g. 1 ~ 5 -> 1 ~ right(3) に絞る
            right = mid
        else:
            # 中間バージョンが正常な場合、右半分に絞る e.g. 1 ~ 5 -> left(3) ~ 5 に絞る
            left = mid + 1

    # leftとrightの値が一致するとループを抜ける それが最初のバッドバージョン
    return left


# サンプルの isBadVersion 関数
def is_bad_version(version):
    # 例として、バッドバージョンが4番目の場合を想定
    return version >= 4


# バージョン数
n = 5

# 最初のバッドバージョンを見つける
first_bad = first_bad_version(n)

print("最初のバッドバージョンは:", first_bad)
