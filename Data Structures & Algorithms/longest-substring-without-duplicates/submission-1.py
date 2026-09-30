class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""

        for i in range(len(s)):
            check = set()
            for j in range(i, len(s)):
                if s[j] in check:
                        break
                else:
                    check.add(s[j])
                    if len(check) > len(res):
                        res = "".join(check)
            
        return len(res)

