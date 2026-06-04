class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for char in s:            
            if char.isalnum():
                lower_char = char.lower()
                cleaned.append(lower_char)
        return cleaned == cleaned[::-1]