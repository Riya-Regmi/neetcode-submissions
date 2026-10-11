import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        i=0
        left=0
        right=len(nums)
        product=1
        while i<len(nums):
            while True:
                if i==left:
                    left+=1
                elif i!=left and left<right:
                    product*=nums[left]
                    left+=1
                elif left==right:
                    output.append(product)
                    left=0
                    product=1
                    i+=1
                elif i==right:
                    return output
                    
        
        




        



        