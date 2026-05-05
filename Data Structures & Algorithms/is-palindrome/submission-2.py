class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase_string = s.lower()
        # cleaned = '' #new string var to only store the string with lowercase letters n digits 
        # #by removing everything else like comma, alpha numeric etc
        # for c in lowercase_string:
        #     if c.isalnum():
        #         cleaned += c
        # reversed_string = cleaned[::-1] #reversing of string
        # if reversed_string == cleaned:
        #     return True
        # else :
        #     return False
        
        #using the 2 pointer efficient solution with no extra space consumption.
        i = 0
        j = len(s) - 1
        while i<j:
            if not s[i].isalnum(): #if s[i] is not alphanumeric skip
                i +=1 
                continue
            if not s[j].isalnum(): #if s[j] is not alphanumeric skip
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True