class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        l = 0
        res = 0

        for idx,  char in enumerate(s):
            while s[idx] in check:
                check.remove(s[l])
                l += 1
            check.add(s[idx])
            res = max(res, idx - l + 1)
        return res
                
        