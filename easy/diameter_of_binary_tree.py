# 二分木の直径（最も長い経路の辺の数）を返す
# 時間計算量：O(N) 空間計算量：O(H) Hは木の高さ 再帰スタック 最悪 O(N)、平衡木なら O(log N)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root):
        ans = 0  # 現在までの最大直径（辺の数）

        def dfs(node):
            nonlocal ans

            if not node:
                return 0  # 高さ0

            # 左右の部分木の高さを取得
            left = dfs(node.left)
            right = dfs(node.right)

            # このノードを通る直径を更新
            ans = max(ans, left + right)

            # 親へ高さを返す
            return max(left, right) + 1

        dfs(root)
        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameter_of_binary_tree(root)) # 3