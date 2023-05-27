# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        d = {}
        node = head
        i = 0
        while node != None:
            d[i % (n+1)] = node
            i += 1
            node = node.next
        i -= 1
        if d[(i- n+1) % (n+1)] == head:
            return head.next
        d[(i- n) % (n+1)].next = d[(i- n+1) % (n+1)].next
        return head

head = ListNode()
node = head
for i in range(1, 10):
    node.next = ListNode(val=i)
    node = node.next

node = head

sol = Solution()
a = sol.removeNthFromEnd(head, 1)

while a != None:
    print(a.val)
    a = a.next