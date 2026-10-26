
# 二分木を上から下へ、各階層を左から右へ探索し、階層ごとにリストにまとめる

# 1. 空の木を判定：root が None なら [] を返す。
# 2. 初期化：queue に root を入れ、result = [] を作る。
# 3. 繰り返し：while queue: でノードがなくなるまで処理する。
# 4. 階層の管理：len(queue) で現在の階層のノード数を取得する。
# 5. ノードを取り出す：queue.popleft() で先頭から取り出す。
# 6. 子ノードを追加：左の子、右の子が存在すれば queue.append() で追加する。
# 7. 結果を保存：現在の階層の値をリストにまとめ、result に追加する。

# - queue：探索待ちのノードを格納
# - level：現在の階層の値を格納
# - result：すべての階層の結果を格納

# 時間・空間計算量: O(n)

from collections import deque

def level_order(root):
    if not root:
        return []

    queue = deque([root])  # 次に処理するノード
    result = [] # 最終結果

    while queue:
        level = []  # 現在階層の値を保持

        # loop開始時にlen(queue)を固定し現在の階層にあるノード数だけ処理 
        for _ in range(len(queue)):
            node = queue.popleft()  # popした値は消える
            level.append(node.val)

            # 追加分は次のloopで処理
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# level_order関数を使用してレベル順のトラバーサルを取得
print(level_order(root)) # 出力: [[3], [9, 20], [15, 7]]
