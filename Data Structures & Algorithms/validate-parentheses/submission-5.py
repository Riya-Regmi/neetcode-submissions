class Solution:
    def isValid(self, s: str) -> bool:
        bracket={
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack=[]
        for i in s:
            if i not in bracket:
                stack.append(i)
            else:
                check=stack.pop(-1)
                if bracket[i]!=check:
                    return False
        return True
                
        

            