
# 二分木において、任意の2ノード間で最も長いパス（直径）の長さ（エッジ数）を求める。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameter_of_binary_tree(self, root):
        # 最大直径を0で初期化
        self.max_diameter = 0

        # 与えられたノードから左右の部分木の高さを再帰的に計算
        def dfs(node):
            # ノードが空なら高さは0
            if not node:
                return 0
            # 左右の子ノードの高さを取得
            left = dfs(node.left)
            right = dfs(node.right)
            # 現在のノードを通る直径を更新（もし大きければ）
            self.max_diameter = max(self.max_diameter, left + right)
            # このノードの高さを返す
            return max(left, right) + 1

        dfs(root)
        return self.max_diameter
    
# サンプルツリー:
#       1
#      / \
#     2   3
#    / \     
#   4   5    

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

sol = Solution()
print(sol.diameter_of_binary_tree(root))  # 出力: 3 (ノード4-2-1-3の経路)
