class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_chars = [char.lower() for char in s if char.isalnum()]
        return clean_chars == clean_chars[::-1] 