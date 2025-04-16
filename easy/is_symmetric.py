
'''
二分木の根ノードが与えられたとき、その木が左右対称（中心を軸に鏡のように反転）かどうかを判定する
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root: TreeNode) -> bool:
    if not root:
        return True
    return is_mirror(root.left, root.right)

def is_mirror(t1: TreeNode, t2: TreeNode) -> bool:
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return (t1.val == t2.val and
            is_mirror(t1.left, t2.right) and
            is_mirror(t1.right, t2.left))

# テスト用の木を作成
# 対称な例:
#        1
#      /   \
#     2     2
#    / \   / \
#   3   4 4   3

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

# 実行
print(is_symmetric(root))  # True が出力される
