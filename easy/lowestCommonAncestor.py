class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    if not root:
        return None

    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
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
ancestor = lowestCommonAncestor(root, p, q)
print(ancestor.val)  # Output: 6

p = TreeNode(2)
q = TreeNode(4)
ancestor = lowestCommonAncestor(root, p, q)
print(ancestor.val)  # Output: 2
