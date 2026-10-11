

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        left=0
        right=len(nums)-1
        while left<len(nums):
            sum=nums[left]+nums[right] 
            if -sum in nums[left+1:right-1] :
                a=[nums[i],nums[j],-sum]
                a=sorted(a)
                if a not in arr:
                    arr.append(a)
                right-=1
            left+=1
        return arr
       
                


                                
        



        
