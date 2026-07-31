# リストの各ノードの向きを反転
# 時間計算量: O(n) 空間計算量: O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None       # 反転済み部分の先頭
    current = head    # 現在処理しているノード

    while current:
        next_node = current.next   # 次のノードを退避
        current.next = prev        # 矢印を逆向きにする
        prev = current             # 反転済み部分を更新
        current = next_node        # 次のノードへ進む

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