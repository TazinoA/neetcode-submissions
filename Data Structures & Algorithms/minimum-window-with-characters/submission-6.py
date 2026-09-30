class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        elif s == t:
            return s
        if len(s) == len(t):
            if t == s:
                return s
            else:
                subFreq = Counter(s)
                freq = Counter(t)
                same_or_greater = True
                for letter in freq:
                    if subFreq[letter] < freq[letter]:
                        same_or_greater = False
                if same_or_greater:
                    return s
                else:
                    return ""
        res = s
        n = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub = set(s[i:j])
                found = True
                for char in t:
                    if char not in sub:
                        found = False
                        n+=1
                        break
                if found:
                    subFreq = Counter(s[i:j])
                    freq = Counter(t)
                    same_or_greater = True
                    for letter in freq:
                        if subFreq[letter] < freq[letter]:
                            same_or_greater = False
                    if same_or_greater:
                        res = min(res, "".join(s[i:j]), key = len)
        if n == (len(s) * (len(s)+1))/2:
            return ""
        return res

        