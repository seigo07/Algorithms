# 二分木subRootと同じ構造・値を持つ部分木が、二分木rootの中に存在するか判定
# 時間計算量：最悪 O(N × M) 空間計算量：最悪 O(N + M) Nはrootのノード数 MはsubRootのノード数

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # ノードの値
        self.left = left    # 左の子ノード
        self.right = right  # 右の子ノード


def is_same(a, b):
    """2つの木の構造と値が完全に同じか判定する"""
    if not a or not b:
        return a is b  # 両方NoneならTrue、片方だけNoneならFalse

    return (
        a.val == b.val
        and is_same(a.left, b.left)
        and is_same(a.right, b.right)
    )


def is_subtree(root, sub_root):
    """rootの中にsub_rootと同じ部分木があるか判定する"""
    if not root:
        return False

    # 現在位置を根とする木を比較。
    # 一致しなければ、左右の部分木を調べる。
    return (
        is_same(root, sub_root)
        or is_subtree(root.left, sub_root)
        or is_subtree(root.right, sub_root)
    )


# root = [3, 4, 5, 1, 2]
root = TreeNode(
    3,
    TreeNode(4, TreeNode(1), TreeNode(2)),
    TreeNode(5)
)

# subRoot = [4, 1, 2]
sub_root = TreeNode(
    4,
    TreeNode(1),
    TreeNode(2)
)

print(is_subtree(root, sub_root))  # True