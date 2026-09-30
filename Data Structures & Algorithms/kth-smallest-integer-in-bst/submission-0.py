# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def recurse(node,res):
            if not node:
                return
            
            recurse(node.left, res)
            res.append(node.val)
            recurse(node.right, res)

            return res
        
        res = recurse(root, [])
        print(res)

        return res[k-1]



        