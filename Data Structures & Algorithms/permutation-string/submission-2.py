class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length=len(s1)
        for i in range(len(s2)):
            text=s2[i:i+length]
            if sorted(text)==sorted(s1):
                return True
            else:
                continue
        return False



        
            
        


        

        

        



            

        
        