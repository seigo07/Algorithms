# 二分木が左右対称か判定
# 時間計算量：O(n)
# 空間計算量：O(h) 同時に保持する関数呼び出しは最大h個 最悪の場合はO(n)、平衡木ならO(log n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # ノードの値
        self.left = left      # 左の子
        self.right = right    # 右の子


def is_symmetric(root):
    # 2つの部分木が互いに鏡映か調べる
    def mirror(left, right):
        # 両方とも空なら対称
        if left is None and right is None:
            return True

        # 片方だけ空なら非対称
        if left is None or right is None:
            return False

        # 値と、外側・内側のノードを比較
        return (
            left.val == right.val
            and mirror(left.left, right.right)
            and mirror(left.right, right.left)
        )

    # 空の木、または左右の部分木が鏡映なら対称
    return root is None or mirror(root.left, root.right)


# root = [1, 2, 2, 3, 4, 4, 3] を作成
root = TreeNode(
    1,
    TreeNode(2, TreeNode(3), TreeNode(4)),
    TreeNode(2, TreeNode(4), TreeNode(3))
)

print(is_symmetric(root))  # True