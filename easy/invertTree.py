# 与えられた二分木の各ノードの左右の子を交換し、二分木全体を反転


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invert_tree(root):
    if root is None:
        return None

    # 左右の子を交換する
    root.left, root.right = root.right, root.left

    # ツリー全体を反転（左右の子ツリーに再帰的に適用）
    # 再帰呼び出しにより、ツリー内のすべてのノードを反転
    invert_tree(root.left)
    invert_tree(root.right)

    return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

root = invert_tree(root)
