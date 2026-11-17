
# candidates の数字を組み合わせて、合計が target になるすべての組み合わせを求める
# 同じ数字は何回使ってもよい。
# 数字の順番が違うだけの組み合わせは重複として扱う。
# 合計が target に一致する組み合わせだけを返す。

# 基本アルゴリズム: バックトラッキング（再帰処理）

# 1. 空の組み合わせから開始する。
# 2. 候補の数字を1つ追加する。
# 3. 合計が target と一致したら結果に保存する。
# 4. 合計が target を超えたら探索を終了する。
# 5. 次の組み合わせを調べるため、追加した数字を取り除いて探索を続ける。
# ポイント： 重複を避けるため、選択した数字より前の候補には戻らない。

# result: 完成した組み合わせの一覧
# start: 探索を開始する候補のインデックス
# path: 現在選択中の数字の組み合わせ
# total: path の数字の合計
# i: 現在調べている候補のインデックス

# 計算量: 
# n = len(candidates)：候補の個数 
# m = target // min(candidates)：最大再帰深度

# 時間計算量: O(mnᵐ) for: 最大O(n) dfs()：最大m段 path.copy()：最大O(m)
# 空間計算量: path(O(m)) + dfs(O(m)) = O(m)

def combination_sum(candidates, target):
    result = []  # 条件を満たす組み合わせ

    def dfs(start, path, total):
        # ① 合計がtargetと一致したら保存
        if total == target:
            result.append(path.copy())
            return

        # ② 合計がtargetを超えたら終了
        if total > target:
            return

        # ③ 候補を順番に探索
        for i in range(start, len(candidates)):
            path.append(candidates[i])  # 数字を追加

            # 同じ数字を再利用できるようiから探索
            dfs(i, path, total + candidates[i])

            path.pop()  # 数字を取り消す

    dfs(0, [], 0)
    return result


# 実行コード
candidates = [2, 3, 6, 7]
target = 7

print(combination_sum(candidates, target))
# [[2, 2, 3], [7]]