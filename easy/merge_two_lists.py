class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2つのソート済み連結リストを、昇順で1つのソートされたリストを作成
# 時間計算量: O(n + m) 空間計算量: O(1)
def merge_two_lists(l1, l2):

    dummy = ListNode()  # 完成リストの最初の固定位置 0 -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
    current = dummy # 初期値はdummy 現在値のみ

    while l1 and l2:
        # 小さい方の要素を新しいリンクリストに追加
        if l1.val < l2.val:
            current.next, l1 = l1, l1.next
        else:
            current.next, l2 = l2, l2.next
        current = current.next

    current.next = l1 or l2 # どちらかのリストがNoneになった場合、残りのリストを追加
    return dummy.next  # dummy 0 -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 dummy.next 1 -> 1 -> 2 -> 3 -> 4 -> 4


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = merge_two_lists(l1, l2)

while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
