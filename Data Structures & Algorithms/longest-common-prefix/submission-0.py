"""
get the smallest string
check every prefix of smallest string and return longest one
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        smallest_string = min(strs, key = len)
        for i in range(len(smallest_string)):
            prefix = smallest_string[0:i+1]
            common = True
            for word in strs:
                if not word.startswith(prefix):
                    common = False
                    break
            if not common:
                break
            else:
                res = prefix
        return res
                