# 二つのソートされたリンクリストをマージして、1つのソートされたリストを作成する


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):

    # マージ操作の簡略化のためのダミーノード
    dummy = ListNode()
    # ポインタを渡す
    current = dummy

    while list1 and list2:
        # 小さい方の要素を新しいリンクリストに追加
        if list1.val < list2.val:
            current.next = list1
            # 次のノードに進める
            list1 = list1.next
        else:
            # current ポインタの次のノードを list2 の現在のノードに設定
            # current ポインタが新しいリストで次に追加されるノードである list2 を指す
            current.next = list2
            # 次のノードに進める
            list2 = list2.next
        # ポインタを次のノードに進める
        # 操作中のリストが入る
        # e.g.
        # 1 -> 3 -> 4 ->
        # 1 -> 2 -> 4 ->
        # 2 -> 4 ->
        # 3 -> 4 ->
        # 4 ->
        current = current.next
        print(current.val)

    # どちらかのリストが空になった場合、残りのリストを追加
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next  # ダミーノードの次のノードを返す（マージされたリストの先頭）


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# リストをマージして、新しいソート済みリンクリストを取得
merged_list = merge_two_lists(list1, list2)

# 結果を出力
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
