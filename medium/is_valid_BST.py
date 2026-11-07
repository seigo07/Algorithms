
# 与えられた二分木が、**二分探索木（BST）**か判定する
# すべての部分木において下記が成立する
# 左の子 < 親
# 右の子 > 親

# 基本アルゴリズム: DFS ＋ 再帰処理

# 処理フロー：
# 1. ルートから探索を開始する。
# 2. 各ノードが許される値の範囲 low < val < high にあるか確認する。
# 3. 左の子には上限を、右の子には下限を更新して渡す。
# 4. 子が None なら True を返す。
# 5. すべてのノードが条件を満たせば True。
# 重要： 親と子だけの比較では不十分です。祖先ノードの制約も引き継ぐ必要があります。

# node	現在確認するノード
# low	許される値の下限
# high	許される値の上限
# node.val	現在のノードの値

# 時間計算量: O(n) 全ノードを1回ずつ見る
# 空間計算量: 再帰スタック分 平均：O(log n) 最悪（片側木）：O(n)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_BST(root):

    # DFSで範囲チェック
    def dfs(node, low, high):

        # nodeがNoneになったら（子がない）OK
        if not node:
            return True

        # BST条件違反（範囲外ならNG）
        if not (low < node.val < high):
            return False

        # 左右を再帰チェック
        return (
            # 左の子は親の値より小さくする（上限更新）
            dfs(node.left, low, node.val) and
            # 右の子は親の値より大きくする（下限更新）
            dfs(node.right, node.val, high)
        )
    
    # 初期範囲は無限
    return dfs(root, float("-inf"), float("inf"))


# 使用例:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

print(is_valid_BST(root))  # True
