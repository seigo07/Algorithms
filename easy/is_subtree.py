
'''
ある二分木 root に、構造とノードの値が同じ部分木 subRoot が含まれるかを判定
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_subtree(root, subRoot):
    if not root:
        return False
    if is_sametree(root, subRoot):
        return True
    # 左右の部分木で再帰的にチェック
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)

def is_sametree(s, t):
    if not s and not t:
        return True
    if not s or not t or s.val != t.val:
        return False
    # 左右のノードの値と構造が一致しているか
    return is_sametree(s.left, t.left) and is_sametree(s.right, t.right)


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

subroot = TreeNode(4)
subroot.left = TreeNode(1)
subroot.right = TreeNode(2)

# --- 結果出力 ---
result = is_subtree(root, subroot)
print("Is subroot a subtree of root?:", result)
