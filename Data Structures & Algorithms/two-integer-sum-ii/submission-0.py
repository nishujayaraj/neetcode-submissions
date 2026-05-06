class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0 
        j = n - 1
        total = 0
        #always while manually controlling the pointers better to use while loop
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i+1,j+1] #we have to return the indexes
            elif total < target:
                i+=1
            else:
                j -= 1
#loop until i and j meet