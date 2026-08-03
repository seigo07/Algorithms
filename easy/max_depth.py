# 二分木の最大の深さを求める
# 時間計算量：O(n) 
# 空間計算量：O(h) h = 木の高さ 再帰呼び出しのスタック 最悪 O(n)、平衡木なら O(log n)
# 新しい配列やリストは作っていないが、再帰呼び出しによりメモリ上に待機している関数の数だけメモリを使う

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # ノードの値
        self.left = left    # 左の子ノード
        self.right = right  # 右の子ノード


def max_depth(root):
        # ノードが存在しない場合、深さは0
        if not root:
            return 0

        # 左右の深さの深い方に現在のノード分(+1)を加えて返す
        return 1 + max(max_depth(root.left),
                       max_depth(root.right))


# Example 1
root = TreeNode(
    3,
    TreeNode(9),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7)
    )
)

print(max_depth(root))   # 3


# Example 2
root = TreeNode(
    1,
    None,
    TreeNode(2)
)

print(max_depth(root))   # 2