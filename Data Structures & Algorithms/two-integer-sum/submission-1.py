class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)): #here i takes the index value of the numbers present in the array
            difference = target - nums[i]

            if difference in seen:
                return [seen[difference], i] #seen[difference] will basically give the index of the number from the dict

            seen[nums[i]] = i 

#check the difference present in the dict 
#but not present save the num[i] in the dict and not the difference