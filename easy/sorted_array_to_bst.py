# 昇順に並んだ配列の中央要素を根として再帰的に分割し、高さの偏りが小さい二分探索木を作成
# 時間計算量：O(n) 空間計算量：O(log n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # ノードの値
        self.left = left    # 左の子
        self.right = right  # 右の子


def sorted_array_to_bst(nums):
    # 二分探索木
    def build(left, right):
        if left > right:  # 子ノードがない
            return None

        mid = (left + right + 1) // 2   # 偶数個の場合は右側の中央を選ぶ

        root = TreeNode(nums[mid])       # 中央要素を根にする
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root

    return build(0, len(nums) - 1)


# 実行例
nums = [-10, -3, 0, 5, 9]
root = sorted_array_to_bst(nums)

print(root.val)        # 0
print(root.left.val)   # -3
print(root.right.val)  # 9

#        0
#       / \
#     -3   9
#     /   /
#   -10  5