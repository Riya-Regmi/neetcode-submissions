from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s3=list(s1)
        for i in s2:
            if i in s1 and i not in s3:
                return False
            elif i in s1 and i in s3:
                s3.remove(i)
            else:
                continue
        return True


        

        

        



            

        
        