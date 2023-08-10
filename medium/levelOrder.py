# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# バイナリ ツリーのルートを指定すると、そのノードの値のレベル順序の走査を返します。 (つまり、左から右へ、レベルごとに)。
# 二分木のノードの値のレベル順のトラバーサルを返すプログラムです。
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        result, queue = [], [root]

        while queue:
            level = []
            level_size = len(queue)
            for i in range(level_size):
                current_node = queue.pop(0)
                level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(level)

        return result


# インスタンスの作成
solution = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# levelOrder関数を使用してレベル順のトラバーサルを取得
print(solution.levelOrder(root)) # 出力: [[3], [9, 20], [15, 7]]
