
# 1〜n のバージョンの中で、最初に壊れたバージョンをできるだけ少ないAPI呼び出しで特定する

# 基本アルゴリズム: Binary Search

# 1. left = 1、right = n で探索範囲を設定。
# 2. mid で中央のバージョンを取得。
# 3. isBadVersion(mid) で判定。
#    - 不良品 → mid を含む左半分を探索。
#    - 正常品 → mid より右半分を探索。
# 4. 探索範囲が1つになるまで繰り返す。
# 5. 最初の不良バージョンを返す。

# 時間計算量: O(log n) 二分探索のため
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
