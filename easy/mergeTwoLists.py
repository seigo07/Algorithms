
'''

2つのソート済み連結リストをマージ

ループごとのcurrentとdummyの遷移（値のみ）
ステップ	current.val	dummy.nextのリスト状態
初期	0（dummy）	空（まだ繋がっていない）
1回目	1	1
2回目	1	1 → 1
3回目	2	1 → 1 → 2
4回目	3	1 → 1 → 2 → 3
5回目	4	1 → 1 → 2 → 3 → 4
6回目	4	1 → 1 → 2 → 3 → 4 → 4

最終結果（dummy.next）: 1 → 1 → 2 → 3 → 4 → 4

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):

    dummy = ListNode()  # マージ後リストの先頭を保持する固定ノード。最初から最後まで不変
    current = dummy # 現在のノード追加位置。マージされたリストの最後尾へ1つずつ進む

    # list1とlist2を比較し、小さい方を結果リストに追加
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1  # 小さい方のノードを繋げ、ポインタを進める
            list1 = list1.next  # list1を次に進める
        else:
            current.next = list2  # 小さい方のノードを繋げ、ポインタを進める
            list2 = list2.next  # list2を次に進める
        current = current.next  # 挿入位置を1つ進める

    current.next = list1 if list1 else list2  # 片方のリストが残っていたら、そのまま繋げる
    return dummy.next  # ダミーノードの次のノードを返す（マージされたリストの先頭）


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# リストをマージして、新しいソート済みリンクリストを取得
merged_list = merge_two_lists(list1, list2)

# 結果を出力
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
