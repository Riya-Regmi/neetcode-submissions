class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket=["{","(","["]
        close_bracket=["}","]",")"]
        stack=[]
        for i in s:
            if i in open_bracket:
                stack.append(i)
            if i in close_bracket:
                check=stack.pop()
                if check!=i:
                    return False
        return True

        

            