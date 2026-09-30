"""
if open less than n and close less than open:
    dfs on both open and close
elif close == open:
    dfs on open
elif open == n and close < n:
    dfs on close
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, openCount, closeCount):
            if openCount == closeCount == n:
                res.append(curr)
                return
            if openCount < n and closeCount < openCount:
                dfs(f"{curr}(", openCount + 1, closeCount)
                dfs(f"{curr})", openCount, closeCount + 1)
            elif closeCount == openCount:
                dfs(f"{curr}(", openCount + 1, closeCount)
            elif openCount == n and closeCount < n:
                dfs(f"{curr})", openCount, closeCount + 1)
        dfs("", 0, 0)
        return res
            