
'''
与えられた一連のバージョンの中から、最初のバッドバージョンを特定する
最小限のAPI呼び出しを行うため、二分探索を使用する
'''


def first_bad_version(n):
    left, right = 1, n

    while left < right:

        # 中央のバージョンを調べる
        mid = left + (right - left) // 2
        print(mid)

        if is_bad_version(mid):
            # 中間バージョンがバッドバージョンである場合、中間値から左半分に探索範囲を絞る
            # e.g. 1 ~ 5 -> 1 ~ right(3) に絞る
            right = mid
        else:
            # 中間バージョンが正常な場合、中間値から右半分に探索範囲を絞る
            # e.g. 1 ~ 5 -> left(3) ~ 5 に絞る
            left = mid + 1

    # leftとrightの値が一致すると、ループを抜ける
    # それが最初のバッドバージョン
    return left


# サンプルの isBadVersion 関数
def is_bad_version(version):
    # 例として、バッドバージョンが4番目の場合を想定
    return version >= 4


# バージョン数
n = 5

# 最初のバッドバージョンを見つける
first_bad = first_bad_version(n)

print("最初のバッドバージョンは:", first_bad) # Output: 4
