# 与えられた二分探索木（Binary Search Tree、BST）内で、
# 与えられた p と q の最小共通の祖先（Lowest Common Ancestor、LCA）を見つける
# BSTは、各ノードが特定の順序で整列された値を持つデータ構造であり、
# LCAは与えられた p と q のノードの共通の祖先のうちで最も深いノードを指す


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    # BSTの性質を利用して、LCAを見つける
    while root:
        if p.val < root.val and q.val < root.val:
            # pとqが現在のrootの値よりも小さい場合、左部分木に移動
            root = root.left
        elif p.val > root.val and q.val > root.val:
            # pとqが現在のrootの値よりも大きい場合、右部分木に移動
            root = root.right
        else:
            # pとqが異なる部分木に存在する場合、LCAは現在のroot
            return root


# 例のためのBSTを作成
#        6
#       / \
#      2   8
#     / \ / \
#    0  4 7 9
#      / \
#     3  5
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = TreeNode(2)
q = TreeNode(8)
ancestor = lowestCommonAncestor(root, p, q)
print(ancestor.val)  # Output: 6

p = TreeNode(2)
q = TreeNode(4)
ancestor = lowestCommonAncestor(root, p, q)
print(ancestor.val)  # Output: 2
