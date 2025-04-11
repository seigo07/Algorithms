
# 連結リストにサイクルがあるかどうかを検出し、存在すれば True を返し、なければ False を返す


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head):
    
    slow = head
    fast = head

    while fast and fast.next:
        # slow は1ノードずつ進みfast は2ノードずつ進む
        slow = slow.next
        fast = fast.next.next
        # slow と fast がどこかでぶつかればサイクルがある。
        if slow == fast:
            return True
    # fast が None に到達したらサイクルはない
    return False


# リンクリストを作成: 1 -> 2 -> 3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# 循環がない場合
result1 = has_cycle(node1)
print("リンクリスト1: 循環があるか？", result1)  # 出力: False

# 循環を作成: 3 -> 2
node3.next = node2

# 循環がある場合
result2 = has_cycle(node1)
print("リンクリスト2: 循環があるか？", result2)  # 出力: True
