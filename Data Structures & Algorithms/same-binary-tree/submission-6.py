# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            curr_p = q1.popleft()
            curr_q = q2.popleft()

            if not curr_p and not curr_q:
                continue
            
            if (not curr_p or not curr_q) or (curr_p.val != curr_q.val):
                return False
            
            q1.append(curr_p.left)
            q1.append(curr_p.right)
            q2.append(curr_q.left)
            q2.append(curr_q.right)


        return True