class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr=[]
        for idx in range(len(nums)-k+1):
            value=nums[idx:idx+k]
            max_value=max(value)
            arr.append(max_value)
        return arr

        