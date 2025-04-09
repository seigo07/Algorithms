# 再帰的なアプローチを使用し、バイナリツリーの各サブツリーにおいて、
# バランス（各ノードの高さの差が1以下）かどうかを判定


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root):
    # ツリーの高さを計算
    def height(node):

        # ノードが存在しない場合、高さは0
        if not node:
            return 0

        # 左部分木の高さを計算
        left_height = height(node.left)

        # 右部分木の高さを計算
        right_height = height(node.right)

        # どちらかの部分木がバランスしていない場合は-1を返す
        # または左右の部分木の高さの差が1を超える場合も-1を返す
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        # ノードの高さを、左右の部分木の高さの最大値に1を加えて更新
        # ex. 使用例1の場合
        # 左部分木の高さ：2
        # 右部分木の高さ：1
        # ルートノードの高さ：max(2, 1) + 1 = 3
        return max(left_height, right_height) + 1

    # ルートノードから始めて、高さがバランスしているかどうかを確認
    return height(root) != -1


# 使用例
# バランスしているツリー
#     1
#    / \
#   2   2
#  / \ / \
# 3  3 3  3
root_balanced = TreeNode(1)
root_balanced.left = TreeNode(2)
root_balanced.right = TreeNode(2)
root_balanced.left.left = TreeNode(3)
root_balanced.left.right = TreeNode(3)
print(is_balanced(root_balanced))  # True

# バランスしていないツリー
#     1
#    / \
#   2   2
#  / \
# 3   3
#    / \
#   4   4
root_unbalanced = TreeNode(1)
root_unbalanced.left = TreeNode(2)
root_unbalanced.right = TreeNode(2)
root_unbalanced.left.left = TreeNode(3)
root_unbalanced.left.right = TreeNode(3)
root_unbalanced.left.left.left = TreeNode(4)
root_unbalanced.left.left.right = TreeNode(4)
print(is_balanced(root_unbalanced))  # False
