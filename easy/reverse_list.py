
# 単方向リストの各ノードの向きを反転

# 3つの変数を使い、ループでポインタを反転する。
# prev: 反転済み部分の先頭
# curr: 現在処理しているノード
# next_node: 次のノードを一時保存

# 1. prev = None、curr = head で初期化
# 2. curr が None になるまで繰り返す
# 3. 次のノードを next_node に保存
# 4. curr.next を prev に変更（向きを反転）
# 5. prev を curr に進める
# 6. curr を next_node に進める
# 7. prev を返す

# 時間計算量: O(n) 空間計算量: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None       # 反転済み部分の先頭
    curr = head    # 現在処理しているノード

    while curr:
        next_node = curr.next   # 次のノードを退避
        curr.next = prev        # 矢印を逆向きにする
        prev = curr             # 反転済み部分を更新
        curr = next_node        # 次のノードへ進む

    return prev


def create_list(values):
    """Pythonのリストから連結リストを作る。"""
    dummy = ListNode()
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def to_list(head):
    """連結リストを表示用のPythonリストに変換する。"""
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


head = create_list([1, 2, 3, 4, 5])
reversed_head = reverse_list(head)

print(to_list(reversed_head))  # [5, 4, 3, 2, 1]