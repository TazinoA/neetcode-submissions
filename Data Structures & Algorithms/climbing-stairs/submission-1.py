class Solution:
    def climbStairs(self, n: int) -> int:

        def helper(n, memo):
            if n <= 2:
                return n
            if n not in memo:
                memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return memo[n]
            
        return helper(n, {})
        