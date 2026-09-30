# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lsts = {}
        
        for i in range(len(lists)):
            lsts[i] = lists[i]
        
        dummy = curr = ListNode()

        while any(node is not None for node in lsts.values()):
            smallest = min(
                (k for k, node in lsts.items() if node is not None),  
                key=lambda k: lsts[k].val
                )
            curr.next = lsts[smallest]
            lsts[smallest] = lsts[smallest].next
            curr = curr.next
        
        return dummy.next

        