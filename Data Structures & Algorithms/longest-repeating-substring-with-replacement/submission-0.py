from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr=list(s)
        i=0
        while i<k:
            for a in range(len(arr)-1):
                if arr[a]!=arr[a+1]:
                    arr[a+1]=arr[a]
                    i+=1

        

            

        

            
                




        
        

                
            

        
        