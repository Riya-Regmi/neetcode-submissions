class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for id,num in enumerate(nums):
            if num==target:
                return id
        return -1