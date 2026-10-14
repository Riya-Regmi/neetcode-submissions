from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen={}
        max_val=0
        for i in s:
            if i not in seen:
                seen[i]=0
            seen[i]+=1 
        if len(seen)==1:
            return len(s)
        else:
            for key,val in seen.items():
                if val>=max_val:
                    max_val=val
            return max_val+k



        

        

           

        



        


             
        


                

                    

                

            
                




        
        

                
            

        
        