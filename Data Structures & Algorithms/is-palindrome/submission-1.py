class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_string = s.lower()
        cleaned = '' #new string var to only store the string with lowercase letters n digits 
        #by removing everything else like comma, alpha numeric etc
        for c in lowercase_string:
            if c.isalnum():
                cleaned += c
        reversed_string = cleaned[::-1] #reversing of string
        if reversed_string == cleaned:
            return True
        else :
            return False