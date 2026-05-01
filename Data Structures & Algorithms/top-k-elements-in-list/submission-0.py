class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        count = {} 
        for i in nums:
            if i not in count: 
                count[i] = 1
            else:
                count[i] += 1  # =+ always resets the value of the key to 1 and += increment the value in dict by 1. 
        sorted_keys = sorted(count, key=lambda x: count[x], reverse=True) #key=lambda x: count[x] means "sort by the frequency of each key, not the key itself."
        #reverse = true means descending order
        return sorted_keys[:k]

#tips : sorted() always returns a list in Python, that is why return statement has [:k]. 