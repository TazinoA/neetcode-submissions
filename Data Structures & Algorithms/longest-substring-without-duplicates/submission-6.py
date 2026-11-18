"""
tmmzuxt
      ^
index_map = {t:0, m:2, z:3, u:4, x:5}
res = 4
l, r = 2, 6
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        res = 0
        l = 0
        for index, letter in enumerate(s):
            if letter not in index_map or index_map[letter] < l:
                index_map[letter] = index
                res = max(res, index - l + 1)
            else:
                l = index_map[letter] + 1
                index_map[letter] = index
        
        return res