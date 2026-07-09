class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 #left pointer
        max_len = 0 
        hashmap = {}
        
        for r in range(len(s)):
            # if s[r] already in window, shrink from left until it's gone
            while s[r] in hashmap:
                del hashmap[s[l]]
                l += 1
            
            # add current character to window
            hashmap[s[r]] = True
            
            # update max window size
            max_len = max(max_len, r - l + 1)
        
        return max_len

#this is a sliding window and 2-pointer leetcode question