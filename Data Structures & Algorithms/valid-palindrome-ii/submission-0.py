"""
on each iteration, remove one character and check if remainder is a palindrome
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        for idx in range(len(s)):
            curr = s[:idx] + s[idx + 1:]
            if self.isPalindrome(curr):
                return True
        return False
    
    def isPalindrome(self, s: str) -> bool:
        res = []

        for char in s:
            if char.isalnum():
                res.append(char.lower())
        
        
        return res == res[::-1]
        