class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word=""
        arr=[]
        count=0
        for i in s:
            if i not in arr and i not in word:
                word+=i
                if len(word)>count:
                    count=len(word)
                arr.append(word)
            else:
                word=""
        return count
        
        
        

                
        
            
            
