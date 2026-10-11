class Solution:

    def encode(self, strs: List[str]) -> str:
        word=""
        for i in strs:
            word+="9"+i # #hello#world#
        word+="9"
        return word


    def decode(self, s: str) -> List[str]:
        output=[]
        if len(s)>0:
            initial=s[0]
            word=""
            for i in s[1:]:
                if i!="9":
                    word+=i
                elif i=="9":
                    output.append(word)
                    word=""
        return output



            



