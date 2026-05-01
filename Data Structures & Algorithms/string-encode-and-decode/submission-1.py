class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "" # initialize an empty string so that you concatinate the encoded strings to it
        for s in strs:
            num = len(s)  
            encoded += f"{num}#{s}"   
        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s): #using while loop to manually control the 2 pointers i,j
            j = i
            while s[j] != '#':  # scan forward until we hit '#'
                j += 1
            length_num = int(s[i:j])        # everything from i to '#' is the length
            word = s[j+1 : j+1+length_num]  # read that many chars after '#'
            result.append(word)
            i = j + 1 + length_num          # jump i forward to next encoded chunk

        return result

# I faced difficulty because, I forgot to use the second pointer 'j'. 