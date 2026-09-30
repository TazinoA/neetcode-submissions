# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
move last k elements to front of list
get pointers to kth element and end of list element
prev of kth element should point to null
end of list element should point to original head
return kth element pointer
[0, 1, 2]
       ^
i = 2
k = 4
length = 3
length - (length % k + 1) - 1 = 3 - (3%4+1) - 1 = 0
point_to_null = 0
kth_element = 1
last_element = 2
"""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head
        length, i = 0, 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        k_eff = k % length
        if k_eff == 0:
            return head
        curr = head
        kth_element, point_to_null = None, None
        while curr.next and i < length:
            if i == length - k_eff - 1:
                point_to_null = curr
                kth_element = curr.next
            i += 1
            curr = curr.next
        last_element = curr

        point_to_null.next = None
        last_element.next = head
        return kth_element
            
