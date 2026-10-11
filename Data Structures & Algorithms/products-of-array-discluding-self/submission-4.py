import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)
        i=0
        output=[]
        product=1
        while i<right:
            if i==left:
                left+=1
            elif i!=left and left<right:
                product*=nums[left]
                left+=1
            elif left==right:
                output.append(product)
                product=1
                left=0
                i+=1
        return output
                    
        
        




        



        