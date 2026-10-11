import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)
        i=0
        output=[]
        for i in nums:
            product=1
            for j in nums:
                if i!=j:
                    product*=j
            output.append(product) 
        return output
            
        
                    
        
        




        



        