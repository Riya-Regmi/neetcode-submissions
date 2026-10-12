class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        while left<right:
            if not s[left].isalnum() and not s[left].isspace():
                left_letter=s[left]
                if not s[right].isalnum() and not s[right].isspace():
                    right_letter=s[right]
                    if left_letter!=right_letter:
                        return False
                    elif left_letter==right_letter:
                        left+=1
                        right-=1
                else:
                    right-=1
            else:
                left+=1
        return True
                
                    
                    

 


        

                