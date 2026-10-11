class Solution:

    def encode(self, strs: List[str]) -> str:
        word=""
        for i in strs:
            word+="@"+i # #hello#world#
        word+="@"
        return word


    def decode(self, s: str) -> List[str]:
        output=[]
        if len(s)>0:
            initial=s[0]
            word=""
            for i in s[1:]:
                if i!="@":
                    word+=i
                elif i=="@":
                    output.append(word)
                    word=""
        return output



            



