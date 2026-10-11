class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i=0
        for i in range(len(nums)):
            if nums[i]  in nums[i+1:]:
                return True
            else:
                i+=1
        return False
        