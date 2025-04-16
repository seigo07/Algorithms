
'''
リンクリストのノードを左右から読み取ったときに同じ順序であれば「回文」と判定し、True を返す。そうでなければ False を返す。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    # 1. fast/slowポインタで中央を探す
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. 後半を反転
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    # 3. 前半と後半（反転済）を比較
    left, right = head, prev
    while right:  # rightの方が短いため
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

# 実行例（1→2→2→1は回文）
def create_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

head = create_linked_list([1, 2, 2, 1])
print(isPalindrome(head))  # True
