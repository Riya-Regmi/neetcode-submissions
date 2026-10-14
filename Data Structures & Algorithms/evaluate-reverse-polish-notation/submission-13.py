import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        token=["+","-","*","/"]
        for i in tokens:
            if i not in token:
                stack.append(int(i)) #33/4
            elif i in token: #/
                a=stack.pop()
                b=stack.pop()
                if i =="+":
                    c=a+b
                    stack.append(c)
                if i == "-":
                    c=b-a
                    stack.append(c)
                if i=="*":
                    c=a*b
                    stack.append(c)
                if i =="/": #13/4
                    c=int(b/a)
                    stack.append(c)
        return stack.pop(-1)


            
        
    
            


        
        