class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next

    return True


# ノードの作成
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# ノードの接続
node1.next = node2
node2.next = node3
node3.next = node4

# 循環の作成
node4.next = node2

# リンクリストに循環があるかどうかをチェック
print(hasCycle(node1))  # これはTrueを出力します

# ノードの作成
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# ノードの接続
node1.next = node2
node2.next = node3

# リンクリストに循環があるかどうかをチェック
print(hasCycle(node1))  # これはFalseを出力します
