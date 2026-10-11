class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=set(nums)
        print(nums)
        left=0
        right=len(nums)-1
        count=0
        counts=[]
        for left in range(len(nums)):
            if nums[left]+1 in nums:
                left+=1
                count+=1
            else:
                counts.append(count)
                count=0
                left=+1
                print(left)
        max_count=max(counts)
        return max_count+1
            


        