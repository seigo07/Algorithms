
'''

BST（Binary Search Tree）におけるLCA（Lowest Common Ancestor：最小共通祖先）
(2つのノード p と q に対して、両方のノードを子孫に持つ最も低い（深い）ノードを探す。
ノード自身が子孫と見なされるため、p または q が共通祖先になることもある。

        6
       / \
      2   8
     / \ / \
    0  4 7 9
      / \
     3  5

例えば、p = 2, q = 8 のとき：
6 は 2 と 8 の間に位置し、両方を子孫に持つ
LCAは 6

p = 2, q = 4 のとき：
4 は 2 の子孫なので、共通祖先は 2
LCAは 2

p.val と q.val が現在のノードの左右に分かれていれば、そこがLCA
両方小さい → 左へ
両方大きい → 右へ

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    # BSTの性質を利用して、LCAを見つける
    while root:
        if p.val < root.val and q.val < root.val:
            # p and q < root -> 左へ
            root = root.left
        elif p.val > root.val and q.val > root.val:
            # p and q > root -> 左へ
            root = root.right
        else:
            # p and qが現在のノードの左右に分かれている場合、現在のrootがLCA
            return root

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = TreeNode(2)
q = TreeNode(8)
ancestor = lowest_common_ancestor(root, p, q)
print(ancestor.val)  # Output: 6

p = TreeNode(2)
q = TreeNode(4)
ancestor = lowest_common_ancestor(root, p, q)
print(ancestor.val)  # Output: 2
