"""
make trust map
for each person check if they trust someone
if not, for everyone else check if they trust said person
if so return the person else continue
at the end return -1
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = defaultdict(int)
        trusted_map = defaultdict(int)
        for a, b in trust:
            trust_map[a] = b
            trusted_map[b] += 1
        
        
        for i in range(1, n+1):
            if not trust_map[i] and trusted_map[i] == n - 1:
                return i
        return -1