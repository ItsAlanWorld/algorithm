class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)


def insertionSortList(head: ListNode) -> ListNode:
    cur = parent = ListNode(0)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next
        cur = parent

    return parent.next

print(insertionSortList(head).val)