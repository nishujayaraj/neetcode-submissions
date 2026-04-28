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
            if v != 0: #you have to add 'if' because without that the moment first v != 0 it throws false, which might not be true always.
                return False
        return True