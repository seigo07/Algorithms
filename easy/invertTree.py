# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root):
    if root is None:
        return None

    # Swap the left and right subtrees
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)

    return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

root = invertTree(root)
