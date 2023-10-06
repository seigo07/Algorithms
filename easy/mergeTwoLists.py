# 二つのソートされたリンクリストをマージして、1つのソートされたリストを作成する


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):

    # 新しいリンクリストの先頭を表すダミーノード（マージ操作の簡略化のために使用）
    dummy = ListNode()
    current = dummy  # 現在のノードをダミーノードに設定

    while list1 and list2:
        # list1とlist2を比較し、小さい方の要素を新しいリンクリストに追加
        if list1.val < list2.val:
            # current ポインタの次のノードを list1 の現在のノードに設定
            # current ポインタが新しいリストで次に追加されるノードである list1 を指す
            current.next = list1
            list1 = list1.next
        else:
            # current ポインタの次のノードを list2 の現在のノードに設定
            # current ポインタが新しいリストで次に追加されるノードである list2 を指す
            current.next = list2
            list2 = list2.next
        # ポインタを次のノードに進める
        current = current.next

    # どちらかのリストが空になった場合、残りのリストを追加
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next  # ダミーノードの次のノードを返す（マージされたリストの先頭）


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# リストをマージして、新しいソート済みリンクリストを取得
merged_list = mergeTwoLists(list1, list2)

# 結果を出力
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
