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
        if not p and q:
            return False
        if not q and p:
            return False
        q1 = deque()
        q2 = deque()

        q1.append(q)
        q2.append(p)
        while q1 and q2:
            curr_q = q1.popleft()
            curr_p = q2.popleft()

            if curr_q.val != curr_p.val:
                return False
            if curr_q.left and not curr_p.left:
                return False
            if curr_q.right and not curr_p.right:
                return False
            if curr_p.left and not curr_q.left:
                return False
            if curr_p.right and not curr_q.right:
                return False
            
            if curr_q.left:
                q1.append(curr_q.left)
            if curr_q.right:
                q1.append(curr_q.right)

            if curr_p.left:
                q2.append(curr_p.left)
            if curr_p.right:
                q2.append(curr_p.right)

        return True

