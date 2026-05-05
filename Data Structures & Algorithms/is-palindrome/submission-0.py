class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_s = s.lower()
        cleaned = ''
        for c in lowercase_s:
            if c.isalnum():
                cleaned += c
        reversed_string = cleaned[::-1]
        if reversed_string == cleaned:
            return True
        else :
            return False