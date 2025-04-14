
'''
2つの二分木 p と q が構造的に同じであり、かつすべてのノードの値も同じかどうかを確認する
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    # 両方のノードが None → 同じとみなす（True を返す）
    if not p and not q:
        return True
    # 片方だけが None → 異なる（False）
    if not p or not q:
        return False
    # 値が異なる → 異なる（False）
    if p.val != q.val:
        return False
    # 左右の子ノードについて再帰的に同様のチェックを行う
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# --- 動作確認用のテストコード ---

# 🌳 p, q: 同じ構造・値の木
#     1
#    / \
#   2   3
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(is_same_tree(p, q))  # True

# 🌳 p2: 左に子を持つ木
#     1
#    /
#   2
p2 = TreeNode(1, TreeNode(2))

# 🌳 q2: 右に子を持つ木
#     1
#      \
#       2
q2 = TreeNode(1, None, TreeNode(2))
print(is_same_tree(p2, q2))  # False
