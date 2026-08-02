# 単方向連結リストの中央ノードを返す
# 中央が2つある場合は2番目を返す
# slow：1回のループで1ノード進む fast：1回のループで2ノード進む
# fastがリストの末尾まで進んだとき、半分の速度で進んでいたslowは中央に到達している
# 時間計算量：O(n) 空間計算量：O(1)

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head

    # slowは1つ、fastは2つずつ進む
    # fastが末尾に着いたとき、slowは中央にいる
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def create_linked_list(values: list[int]) -> Optional[ListNode]:
    """Pythonのリストから連結リストを作る"""
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def to_list(head: Optional[ListNode]) -> list[int]:
    """連結リストをPythonのリストに変換する"""
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# Example 1
head1 = create_linked_list([1, 2, 3, 4, 5])
middle1 = middle_node(head1)
print(to_list(middle1))  # [3, 4, 5]

# Example 2
head2 = create_linked_list([1, 2, 3, 4, 5, 6])
middle2 = middle_node(head2)
print(to_list(middle2))  # [4, 5, 6]