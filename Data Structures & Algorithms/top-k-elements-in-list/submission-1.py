class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        output=[]
        for i in nums:
            if i not in seen:
                seen[i]=0
            seen[i]+=1
        sorted_data = sorted(seen.items(), key=lambda item: item[1],reverse=True)
        for key in sorted_data[:k]:
            output.append(key[0])
        return output



        