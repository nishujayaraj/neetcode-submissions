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

        while i < len(s):
            j = i
            while s[j] != '#':  # scan forward until we hit '#'
                j += 1
            length = int(s[i:j])        # everything from i to '#' is the length
            word = s[j+1 : j+1+length]  # read that many chars after '#'
            result.append(word)
            i = j + 1 + length          # jump i forward to next encoded chunk

        return result