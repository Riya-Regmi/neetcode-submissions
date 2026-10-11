import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for id,num in enumerate(nums):
            product=1
            if id!=0:
                arr=nums[:id]+nums[id+1:]
            elif id==0:
                arr=nums[id+1:]
            product=math.prod(arr)
            output.append(product)
        return output

        



        