class Solution:

    def encode(self, strs: List[str]) -> str:
        word=""
        encoded_word=[]
        for i in strs:
            length=str(len(i)) + "#" + i
            encoded_word.append(length)
        return encoded_word # 5#Hello5#world
            



    def decode(self, s: str) -> List[str]: # 5#Hello5#world
        left=0
        right=len(s)-1 #13
        output=[]
        while left<right: # left=7 #right=13
            num=int(s[left]) #num=5
            length=left+num+1 #length=7+5+1=13
            word=s[left+2:length+1] #9:13
            output.append(word)
            left=length+1 #14
        return output

            





            



