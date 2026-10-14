class Solution:
    def isValid(self, s: str) -> bool:
        bracket={
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack=[]
        if len(s)==1:
            return False
        for i in s:
            if i not in bracket:
                stack.append(i)
            elif i in bracket and len(stack)!=0:
                check=stack.pop()
                if bracket[i]!=check:
                    return False
            elif len(stack)==0:
                return False
        return True
                
        

            