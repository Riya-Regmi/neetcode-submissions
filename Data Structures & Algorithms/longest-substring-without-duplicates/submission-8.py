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
                index=word.find(i)#1
                word=word[index+1:]
                
        return count
                

            
        
        
        
        

                
        
            
            
