class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums) # prefix[i] = product of everything to the LEFT of i
        suffix = [1] * len(nums) # suffix[i] = product of everything to the RIGHT of i
        output = []

        # build prefix left to right
        # start from i=1 because prefix[0] = 1 (nothing to the left of index 0)
        # range(1, len(nums)) → i = 1, 2, 3 (excludes len(nums) but includes last index)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        # build suffix right to left
        # start from len(nums)-2 because suffix[last] = 1 (nothing to the right of last index)
        # range(len(nums)-2, -1, -1) → i = 2, 1, 0
        # stop is -1 (not 0) because range excludes stop, so -1 ensures we include index 0
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        # multiply prefix and suffix for each position
        # output is empty list so use append, not index
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])

        return output