# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# 二分木のルートを指定して、それが有効な二分探索木 (BST) であるかどうかを判断します。
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root, min_val=float('-inf'), max_val=float('inf')):
        if not root:
            return True

        if not (min_val < root.val < max_val):
            return False

        return self.isValidBST(root.left, min_val, root.val) and self.isValidBST(root.right, root.val, max_val)


# インスタンスの作成
solution = Solution()

# 使用例:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(solution.isValidBST(root))  # Trueを返すべきです
