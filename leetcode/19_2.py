# THIS SOLUTION WASNT MADE BY ME, IT JUST WAS ONE OF THE TOP SOLUTIONS ON THE WEBSITE
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head:
            slowPointer = head
            fastPointer = head

            while n>0 and fastPointer:
                fastPointer = fastPointer.next
                n -= 1
    
            while fastPointer and fastPointer.next:
                slowPointer = slowPointer.next
                fastPointer = fastPointer.next

            if slowPointer == head and not fastPointer:
                return head.next # empty list

            slowPointer.next = slowPointer.next.next

            return head
