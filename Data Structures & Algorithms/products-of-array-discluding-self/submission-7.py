import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        seen={}
        output=[]
        for i in range(len(nums)):
            product=math.prod(nums[i+1:])
            seen[i]=product
        for i in range(len(nums)):
            product=math.prod(nums[:i])
            value=seen[i]*product
            output.append(value)
        return output


               
            
            
            
        
                    
        
        




        



