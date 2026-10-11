class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=tokens[0]
        for idx,i in enumerate(tokens): 
            if i!="+" and i!="-" and i!="*" and i!="/":
                b=a
                a=int(i)
            elif i=="+":
                b=b+a
                tokens.insert(idx+1,b)
            elif i=="-":
                b=b-a
                tokens.insert(idx+1,b)
            elif i=="*":
                b=b*a
                tokens.insert(idx+1,b)
            elif i=="/":
                b=b/a
                tokens.insert(idx+1,b)
        return b
    
            


        
        