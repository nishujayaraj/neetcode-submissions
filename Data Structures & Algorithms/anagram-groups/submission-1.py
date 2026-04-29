class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {} 
        for strings in strs:
            alphabets = [0] * 26 # do the array of size 26 for - 26 alphabets 

            for char in strings:
                alphabets[ord(char)-ord('a')]+=1 # google this line to know "why" always 
            key = tuple(alphabets) #array is mutaable and hence convert it into tuple to use it as a key in dict

            if key not in output:
                output[key] = []

            output[key].append(strings) # tuple go as key and strings (which are anagrams )get appended to the same key in the form of list

        return list(output.values())
             
        