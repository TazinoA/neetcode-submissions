# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
3 -> 5
^
i = 1
1 2
reverse nodes between left and right
old left points to right.next
original left.prev points to head of rev
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseList(root, end):
            prev, curr = None, root
            i = 0
            while curr and i <= end:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                i += 1
            return prev
        if not head.next or left == right:
            return head
        i = 0
        dummy = ListNode(0, head)
        curr, tmp, start = dummy, None, None
        
        while curr:
            if i == left - 1:
                start = curr
                tmp = curr.next
                
            if i == right:
                newTail = curr.next
                newHead = reverseList(tmp, right-left)
                start.next = newHead
                tmp.next = newTail
                break
            
            curr = curr.next
            i += 1
        return dummy.next

        