class Solution:

    def encode(self, strs: List[str]) -> str:
        word=""
        encoded_word=[]
        for i in strs:
            length= str(len(i))+"_encoded_" + i
            encoded_word.append(length)
        return "".join(encoded_word) # 5#Hello5#world

    def decode(self, s: str) -> List[str]:
        left=0
        right=len(s)-1
        output=[]
        while left<right:
            index=s.find("_encoded_",left)
            num=s[left:index]
            l=len(num)
            length=left+l+9+int(num)
            word=s[left+l+9:length]
            output.append(word)
            left=length
        return output