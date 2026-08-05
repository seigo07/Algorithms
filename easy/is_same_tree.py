# 2つの二分木が構造（形）各ノードの値の両方が完全に一致しているか判定（DFS＋再帰）
# 時間計算量 O(n) 空間計算量 O(h) h：木の高さ 再帰スタック分だけ使用
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # ノードの値
        self.left = left    # 左の子ノード
        self.right = right  # 右の子ノード


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    # 両方とも存在しないなら同じ
    if not p and not q:
        return True

    # 片方だけ存在しない、または値が違うなら異なる
    if not p or not q or p.val != q.val:
        return False

    # 左右の部分木が両方とも同じなら同じ木
    return ( is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right) )


# 木を作成
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

# 実行
print(is_same_tree(p, q))