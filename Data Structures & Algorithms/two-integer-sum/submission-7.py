class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output=[]
        for left in range(len(nums)):
            sum=target-nums[left]
            if sum in nums[left+1:]:
                index = nums.index(sum, left + 1)
                output=[left,index]
            else:
                continue
        return output
            





        