
'''
ある二分木 root に、構造とノードの値が同じ部分木 subRoot が含まれるかを判定
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root, subRoot):
    if not root:
        return False
    if isSameTree(root, subRoot):
        return True
    # 左右の部分木で再帰的にチェック
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

def isSameTree(s, t):
    if not s and not t:
        return True
    if not s or not t or s.val != t.val:
        return False
    # 左右のノードの値と構造が一致しているか
    return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)


# --- テスト用の木構造を定義 ---
# root tree:
#        3
#       / \
#      4   5
#     / \
#    1   2

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

# subRoot tree:
#      4
#     / \
#    1   2

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

# --- 結果出力 ---
result = isSubtree(root, subRoot)
print("Is subRoot a subtree of root?:", result)
