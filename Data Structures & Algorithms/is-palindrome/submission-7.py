class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []

        for letter in s:
            if letter.isalnum():
                res.append(letter.lower())
                       
        
        return res == res[::-1]