class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {} 
        for strings in strs:

            alphabets = [0] * 26 

            for char in strings:
                alphabets[ord(char)-ord('a')]+=1
            key = tuple(alphabets)

            if key not in output:
                output[key] = []

            output[key].append(strings)

        return list(output.values())
             
        