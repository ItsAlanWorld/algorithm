head = [2,1,3,5,6,4,7]
result = []
result2 = []
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)

    def sorting(self):
        node = self.head
        cnt = 0
        while node:
            if cnt % 2 == 0:
                result.append(node.val)
                node = node.next
                cnt += 1
            else:
                result2.append(node.val)
                node = node.next
                cnt += 1
        result.extend(result2)


ll = LinkedList()
for i in head:
    ll.append(i)

ll.sorting()
print(result)



