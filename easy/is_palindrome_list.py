# 単方向連結リストの値を逆順にしたものと一致するか比較して回文か判定
# 時間・空間計算量：O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome_list(head):
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    return values == values[::-1]


# Example 1: [1, 2, 2, 1] の連結リストを作成
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

print(is_palindrome_list(head))  # True