class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #dvdf
        word=""
        count=0
        for i in s:
            if i not in word:
                word+=i
                if len(word)>count:
                    count=len(word)
            else:
                word=i
                
        return count
                

            
        
        
        
        

                
        
            
            
