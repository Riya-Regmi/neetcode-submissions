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
            elif  i in bracket:
                try:
                    check=stack.pop(-1)
                    if check!=bracket[i]:
                        return False
                except:
                    return False
        if len(stack)==0:
            return True
        else:
            return False

                
        

            