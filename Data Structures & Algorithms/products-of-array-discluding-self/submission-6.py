import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right=len(nums)-1  #3
        product=1
        left=0
        output=[]
        while left<=len(nums)-1: # 0<3
            if right!=left and right!=-1: # 0!=0
                product=product * nums[right] #1*6*4*2
                right-=1  #0
            elif right==-1:
                output.append(product) 
                product=1 
                left+=1 
                right=len(nums)-1 
            elif right==left:
                right-=1 #-1
        return output
        
               
            
            
            
        
                    
        
        




        



