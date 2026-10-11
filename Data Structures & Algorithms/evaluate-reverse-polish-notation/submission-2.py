class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=int
        b=int
        c=int
        for idx,i in enumerate(tokens): #["1","2","+","3","*","4","-"]
            if i!="+" and i!="-" and i!="*" and i!="/":
                b=a
                a=int(i)
                tokens.pop(idx)
            else:
                tokens.pop(idx)
                bi=a 
                tokens.insert(0,b)
        return b


        
        