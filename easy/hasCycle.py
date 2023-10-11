# 与えられたリンクリストに循環（サイクル）があるかどうかを検出
# リンクリスト内のノードは、次のポインタを辿ることで連続して再び到達できる場合循環である


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycle(head):

    # リストが空、またはノードが1つしかない場合、循環はない
    if not head or not head.next:
        return False

    slow = head  # slowポインタは1つずつ進む
    fast = head.next  # fastポインタは2つずつ進む

    # スローポインタとファーストポインタが一致するまで繰り返します
    while slow != fast:

        # ファーストポインタが末尾に到達する前にNoneになった場合、循環はない
        if not fast or not fast.next:
            return False

        # 循環チェックのため、スローポインタは1つ進み、ファーストポインタは2つ進む
        slow = slow.next
        fast = fast.next.next

    # スローポインタとファーストポインタが一致した場合、循環がある
    return True


# リンクリストを作成: 1 -> 2 -> 3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# 循環がない場合
result1 = hasCycle(node1)
print("リンクリスト1: 循環があるか？", result1)  # 出力: False

# 循環を作成: 3 -> 2
node3.next = node2

# 循環がある場合
result2 = hasCycle(node1)
print("リンクリスト2: 循環があるか？", result2)  # 出力: True
