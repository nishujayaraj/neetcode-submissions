class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {} #using dict instead of set() because set() doesnot allow repeated characters, maintains uniqueness. 
        for char in s:
            count[char] = count.get(char , 0) + 1
        for char in t:
            count[char] = count.get(char , 0) - 1
        for v in count.values():
            if v != 0: #without "if", you return on the very first value regardless of whether it's 0 or not, cutting the loop short.
                return False
        return True