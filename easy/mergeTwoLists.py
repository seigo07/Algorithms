class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy=ListNode(-1)
    prev=dummy
    while list1 and list2:
        if list1.val<list2.val:
            prev.next, list1 = list1, list1.next
        else:
            prev.next, list2 = list2, list2.next
        prev = prev.next

    prev.next = list1 if list1 else list2

    return dummy.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

merged = mergeTwoLists(list1, list2)
current = merged

while current:
    print(current.val, end=",")
    current = current.next
print("None")
