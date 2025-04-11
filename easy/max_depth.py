
# 与えられた二分木のルートノードから一番深い葉ノードまでの**ノード数（深さ）**を再帰的に調べ、最大深さを返す


# 木構造のノード定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 最大深さを求める関数
def max_depth(root):
    if root is None:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1

# --- 実行例 ---
# 以下の二分木を作成：
#       1
#      / \
#     2   3
#    /
#   4
# 木の最大深さは 3（1→2→4）

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)

# 関数の実行と出力
print("最大深さ:", max_depth(tree))  # 出力: 最大深さ: 3
