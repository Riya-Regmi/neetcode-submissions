class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        while True:
            while left<len(nums):
                sum=nums[left]+nums[right]
                if sum==target:
                    output=[left,right]
                    return output
                else:
                    right-=1
            left+=1
                
        return []
            
            





        