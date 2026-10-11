from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        word=list(s1)
        for i in s2:
            if i in s1 and i  in word:
                word.remove(i)
            elif i in s1 and i not in word:
                return False
        return True

        

        



            

        
        