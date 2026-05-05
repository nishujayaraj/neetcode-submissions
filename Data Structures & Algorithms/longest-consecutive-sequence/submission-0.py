class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums) # no dictionary or sorting required, convert the array to set and it's automatically sorted.
        longest_subsequence = 0 
        current_subsequence = 0
        for num in new_nums:
            if num-1 not in new_nums:
                current_subsequence = 1
                while num+1 in new_nums:
                    current_subsequence += 1 
                    num += 1 #value of num is incremented by 1 
                longest_subsequence = max(longest_subsequence, current_subsequence)
        return longest_subsequence 
            
                
#to understand this problem - [2,4,10,3,6,5,22,21] use this array example and walk through.