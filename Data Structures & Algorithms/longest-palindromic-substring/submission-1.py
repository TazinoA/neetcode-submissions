class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

        for word in substrings:
            if self.isPalindrome(word):
                res = max(res, word, key = len)
        return res
    

    
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]      