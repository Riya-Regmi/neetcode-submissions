class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        output=[]
        for i in nums:
            if i not in seen:
                seen[i]=0
            seen[i]+=1
        for key,vals in seen.items():
            if vals>=k:
                output.append(key)
        return output

        