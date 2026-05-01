class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            new_list = nums.copy()
            new_list.pop(i)
            product = math.prod(new_list)
            output.append(product)
        return output
        