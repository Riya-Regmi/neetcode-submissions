class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # 1. Check if the LEFT half is sorted normally
            if nums[l] <= nums[m]:
                # Is the target hiding in this left sorted half?
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Go left
                else:
                    l = m + 1  # Go right
                    
            # 2. Otherwise, the RIGHT half must be sorted normally
            else:
                # Is the target hiding in this right sorted half?
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Go right
                else:
                    r = m - 1  # Go left
                    
        return -1