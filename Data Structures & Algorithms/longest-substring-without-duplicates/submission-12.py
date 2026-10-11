class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #advdf
        word=""
        count=0
        if s[0]==s[1]:
            s=s[1:]
        for idx,i in enumerate(s):
            if i not in word:
                word+=i
                if len(word)>count:
                    count=len(word)
            else:
                index=word.find(i)#1
                word=word[index+1:]
        return count
                

            
        
        
        
        

                
        
            
            
