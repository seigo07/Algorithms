
# リンクリストに循環（サイクル）があるかどうかを判定
# slow は1歩、fast は2歩進む
# 2つが出会う → 循環あり
# fast が末尾に到達 → 循環なし

# 1. slow と fast を head に設定
# 2. slow を1つ、fast を2つ進める
# 3. 同じノードなら True
# 4. 末尾に到達したら False

# 時間計算量: O(n) 空間計算量: O(1)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head):

    slow = fast = head

    while fast and fast.next:

        slow = slow.next          # 1歩進む
        fast = fast.next.next     # 2歩進む
        if slow == fast:          # 出会えば循環あり
            return True

    return False                  # fast が末尾に到達したら循環なし      


# 循環がない場合
# リンクリストを作成: 1 -> 2 -> 3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
result1 = has_cycle(node1)
print(result1)  # 出力: False

# 循環を作成: 3 -> 2
node3.next = node2
result2 = has_cycle(node1)
print(result2)  # 出力: True
