
# 2つの昇順Listを1つに結合

# 基本アルゴリズム: Two Pointers

# 1. 2つのリストの先頭ノードを比較する。
# 2. 小さい方を結果のリストにつなぐ。
# 3. 選んだリストのポインタを次へ進める。
# 4. 片方が空になるまで繰り返す。
# 5. 残っているノードを最後につなぐ。

# 時間計算量: O(n + m) 空間計算量: O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1, l2):

    dummy = ListNode()  # 完成リストの先頭の固定ポインタ(currentは上書きされていくため必要) 0 -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
    current = dummy # 今どこまで作ったかを示す作業用ポインタ（移動時に最後のノードで上書きされる）

    # ex. dummy（最初の位置から動かない）
    #   ↓
    # [0] → [1] → [1] → [2]
    #                     ↑
    #                   current（現在値のみ追いかける）

    while l1 and l2:
        # l1 と l2 の先頭を比較して、小さい方の要素を新しいリストに追加するだけ
        # 1 vs 1 → 1
        # 2 vs 1 → 1
        # 2 vs 3 → 2
        # 4 vs 3 → 3
        # 4 vs 4 → 4
        # 残り   → 4
        if l1.val < l2.val:
            current.next, l1 = l1, l1.next
        else:
            current.next, l2 = l2, l2.next
        current = current.next # currentを追加したノードまで進める

    current.next = l1 or l2 # どちらかのリストがNoneになった場合、残りのリストを追加
    return dummy.next  # dummy 0 -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 dummy.next 1 -> 1 -> 2 -> 3 -> 4 -> 4


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = merge_two_lists(l1, l2)

while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
