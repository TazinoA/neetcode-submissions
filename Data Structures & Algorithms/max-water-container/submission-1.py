class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        res = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)+1):
                sub = heights[i:j]
                amount = min(sub[0], sub[-1]) * (j - i -1)
                res = max(res, amount)
        return res
        