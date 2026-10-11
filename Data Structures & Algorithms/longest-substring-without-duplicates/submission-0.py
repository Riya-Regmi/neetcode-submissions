class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr=[]
        unique=set()
        l=0
        word=""
        for i in s: 
            if i not in unique:
                unique.add(i)
                if i not in arr:
                    word+=i
                    arr.append(word)
            else:
                word=i
                    
        return len(max(arr))

                
        
            
            
