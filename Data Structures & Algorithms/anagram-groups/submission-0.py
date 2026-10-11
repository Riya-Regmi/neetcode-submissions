class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        output=[]
        for i in strs:
            a="".join(sorted(i))
            if a not in seen:
                seen[a]=[]
            seen[a].append(i)
        for key,vals in seen.items():
            output.append(vals)
        return output
                

        

        