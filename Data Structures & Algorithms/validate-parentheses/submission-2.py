class Solution:
    def isValid(self, s: str) -> bool:
        bracket={
            "{":"}",
            "[":"]",
            "(":")"
        }
        if len(s)%2!=0:
            return False
        left=0
        right=len(s)-1
        while left<right:
            value=bracket[s[left]]
            if value in s:
                left+=1
                right-=1
            else:
                return False
        return True