"""
loop through the array
sort the string and add to a set
if sorted string in set add it to anagram group
keep a dict with anagram group indexes in the result array
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_index = {}
        groups = set()
        res = []

        for word in strs:
            group = tuple(sorted(word))
            if group in groups:
                res_index = group_index[group]
                res[res_index].append(word)
            else:
                groups.add(group)
                res.append([word])
                group_index[group] = len(res) - 1
        
        return res