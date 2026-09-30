class Solution:
    def longestPalindrome(self, s: str) -> str:
        substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if self.isPalindrome(s[i:j])]

        return max(substrings, key = len)
    

    
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]      