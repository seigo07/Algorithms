
# 単方向リンクリストの先頭ノードが与えられたときに、中央のノード（中央が2つなら後ろ側） を返す


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    # 2ポインタ法（高速・低速）を使う
    slow = fast = head
    # slow は1ステップずつ、fast は2ステップずつ進む
    while fast and fast.next:   # fast が末尾に到達したとき、slow は中央にいる
        slow = slow.next
        fast = fast.next.next
    return slow

# 実行用テストケースを作成
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print("Linked List:", vals)

# テスト用リンクリスト [1, 2, 3, 4, 5, 6]
head = create_linked_list([1, 2, 3, 4, 5, 6])
print_linked_list(head)
mid = middleNode(head)
print("Middle Node Value:", mid.val) # Output: 4
