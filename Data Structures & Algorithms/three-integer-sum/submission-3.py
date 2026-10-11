

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if -sum in nums[j:] and nums[j]!=sum:
                    a=[nums[i],nums[j],-sum]
                    a=sorted(a)
                    if a not in arr:
                        arr.append(a)
        return arr
       
                


                                
        



        
