class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二分探索木（BST: Binary Search Tree）が有効か確認
# 左の子 < 親
# 右の子 > 親
# すべての部分木でも同じ
# 時間計算量: O(n) 全ノードを1回ずつ見る
# 空間計算量: 再帰スタック分 平均：O(log n) 最悪（片側木）：O(n)
def isValidBST(root):

    # DFSで範囲チェック
    def dfs(node, low, high):

        # nodeがNoneになったら（子がない）OK
        if not node:
            return True

        # BST条件違反
        if not (low < node.val < high):
            return False

        # 左右を再帰チェック
        return (
            dfs(node.left, low, node.val) and
            dfs(node.right, node.val, high)
        )
    
    # 初期範囲は無限
    return dfs(root, float("-inf"), float("inf"))


# 使用例:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

print(isValidBST(root))  # True
