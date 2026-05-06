class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        result = [] #we want all the possible triplets and not just 1st possible one

        for i in range(n):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]: #check for the duplication of i
                continue
            j = i + 1
            k = n - 1
            while j < k:
                total = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if total == 0:
                    result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    while j < k and sorted_nums[j] == sorted_nums[j+1]: #check for the duplication of j
                        j += 1
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result
#this problem is just like 2 sum like previously 
#you use i,j,k pointers but i will be fixed once and j and k will keep moving.
#go through the logic with an example u will understand more better.