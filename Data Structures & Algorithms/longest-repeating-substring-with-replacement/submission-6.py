"""
AAABABB
     ^

k = 0

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        l = 0
        seen = {}

        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]] = 0
            seen[s[r]] += 1

            while (r-l+1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)


        return res