
# 入力 nums = [1, 2, 3] から、数字を重複して使わず、すべての並び順を生成する。

# 基本アルゴリズム: バックトラッキング（再帰処理）

# 1. 空の配列 [] から開始
# 2. 未使用の数字を1つ追加
# 3. 未使用の数字を追加する処理を繰り返す
# 4. すべての数字を使ったら結果に保存
# 5. 最後の数字を取り消し、別の数字で同じ処理を繰り返す
# 6. すべての順列を生成したら終了

# 時間計算量: O(n x n!)
# 再帰: 順列はO(n!)
# for, num in path, path[:]のコピーでそれぞれO(n)

# 空間計算量: O(n x n!) 最も大きい result が支配的
# result	O(n * n!)	n!通りの順列を各n個保存
# path	O(n)	最大n個の数字を保持
# 再帰スタック	O(n)	最大n階層の再帰呼び出し

def permute(nums):
    result = []  # 完成した順列

    def backtrack(path):
        # 全数字を使ったら保存
        if len(path) == len(nums):
            result.append(path[:])
            return

        for num in nums:
            # 使用済みの数字はスキップ
            if num in path:
                continue

            path.append(num)  # 数字を追加
            backtrack(path)   # 再帰処理
            path.pop()        # 追加を取り消す

    backtrack([])
    return result


# 実行
nums = [1, 2, 3]
print(permute(nums))

