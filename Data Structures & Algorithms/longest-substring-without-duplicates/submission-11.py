class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #advdf
        word=""
        count=0
        for idx,i in enumerate(s):
            if i not in word:
                word+=i
                if len(word)>count:
                    count=len(word)
            else:
                word=i
                
        return count
                

            
        
        
        
        

                
        
            
            
