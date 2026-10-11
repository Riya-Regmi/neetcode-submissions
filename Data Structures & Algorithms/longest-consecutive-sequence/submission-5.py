class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=list(set(nums))
        nums=sorted(nums)
        count=0
        small=nums[0]
        for i in nums[1:]:
            if i-1  in nums and i<small:
                small=i
            if small+1  in nums:
                count+=1
                small+=1
        return count+1
            


        