
'''

与えられた単方向リンクリストを後ろから前に逆順にし、新しい先頭ノード（反転後のリストのhead）を返す

ex.
初期状態
prev = None
curr = 1 -> 2 -> 3 -> 4 -> 5

1回目ループ
next_node = 2
curr.next = None
prev = 1
curr = 2

2回目ループ
next_node = 3
curr.next = 1
prev = 2
curr = 3

3回目ループ
next_node = 4
curr.next = 2
prev = 3
curr = 4

4回目ループ
next_node = 5
curr.next = 3
prev = 4
curr = 5

5回目ループ
next_node = None
curr.next = 4
prev = 5
curr = None（終了）

最終状態
prev = 5 -> 4 -> 3 -> 2 -> 1 -> None
→ これが反転後のhead

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None # 逆順で構築中の新しいリンク先
    curr = head # 現在のノードをheadからスタート
    # 現在のノードが存在する限りループ
    while curr:
        next_node = curr.next  # 次のノードを保持
        curr.next = prev       # 現在のノードの次を前のノードに変更（反転）
        prev = curr            # prevを一つ前に進める
        curr = next_node       # 現在のノードを次のノードに進める
    return prev  # 新しいhead


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# リスト作成: 1 -> 2 -> 3 -> 4 -> 5 -> None
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

print("Before reverse:")
print_list(head)

reversed_head = reverse_list(head)

print("After reverse:")
print_list(reversed_head)
