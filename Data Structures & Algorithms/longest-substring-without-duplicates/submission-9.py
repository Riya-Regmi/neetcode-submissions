class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #advdf
        word=""
        count=0
        for idx,i in enumerate(s):
            word+=i
            if i not in word:
                if len(word)>count:
                    count=len(word)
            else:
                index=word.find(i)#1
                word=word[index+1:]
                
        return count
                

            
        
        
        
        

                
        
            
            
