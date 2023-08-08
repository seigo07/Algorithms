class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root):
    def check(root):
        if root is None:
            return 0, True

        left_height, left_balanced = check(root.left)
        right_height, right_balanced = check(root.right)

        return max(left_height, right_height) + 1, left_balanced and right_balanced and abs(left_height - right_height) <= 1

    return check(root)[1]

# 高さバランスされた二分木
root_balanced = TreeNode(1)
root_balanced.left = TreeNode(2)
root_balanced.right = TreeNode(3)
root_balanced.left.left = TreeNode(4)
root_balanced.left.right = TreeNode(5)
root_balanced.right.left = TreeNode(6)
root_balanced.right.right = TreeNode(7)

print(isBalanced(root_balanced))  # Trueを出力

# 高さバランスされていない二分木
root_unbalanced = TreeNode(1)
root_unbalanced.left = TreeNode(2)
root_unbalanced.right = TreeNode(3)
root_unbalanced.left.left = TreeNode(4)
root_unbalanced.left.left.left = TreeNode(5)

print(isBalanced(root_unbalanced))  # Falseを出力
