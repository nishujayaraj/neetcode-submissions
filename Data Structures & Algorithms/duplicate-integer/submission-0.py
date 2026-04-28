class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #using set() instead of dict because set() stores only keys but dict needs key:value pair
        for i in nums:
            if i in seen:
                return True 
            else: 
                seen.add(i)

        return False
        