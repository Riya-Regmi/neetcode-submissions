import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        seen={0:[nums[0]]}
        product=1
        output=[]
        for i in range(1,len(nums)):
            product=product*nums[i-1]
            seen[i]=[product]
        seen[len(nums)-1].append(1)
        p=1
        for i in range(len(nums)-2,-1,-1):
            p=p*nums[i+1]
            seen[i].append(p)
        for i in range(len(nums)):
            a=seen[i]
            p=a[0]*a[1]
            output.append(p)
        return output


        




           

               
            
            
            
        
                    
        
        




        



