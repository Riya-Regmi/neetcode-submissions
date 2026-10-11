class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=int(tokens[0])
        b=a
        for idx,token in enumerate(tokens[1:]):
            if token=="+":
                a=b+a #3
            elif token=="-":
                a=b-a 
            elif token=="*":
                a=b*a#a=9
            elif token=="/":
                a=b/a
            else:
                b=a #9
                a=int(token) #4
        return a

            
        
    
            


        
        