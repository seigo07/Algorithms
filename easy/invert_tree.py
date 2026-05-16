# 与えられた二分木の各ノードの左右の子を交換し、二分木全体を反転
# 時間計算量: O(n)全ノードを1回見る
# 空間計算量: O(h) 再帰スタックの深さ。h は木の高さ
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 木全体を上から順に左右反転する
def invert_tree(root):
    if root is None:
        return None

    # 左右の子を入れ替える
    root.left, root.right = root.right, root.left

    # 左右の部分木も再帰的に反転
    invert_tree(root.left)
    invert_tree(root.right)

    return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

root = invert_tree(root)
