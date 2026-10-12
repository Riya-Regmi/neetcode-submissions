class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=""
        reversed_word=""
        for char in s: #t
            if char.isalnum():
                word=word+char #tabacat
                reversed_word=char+reversed_word #tacabat
        if word.lower()==reversed_word.lower():
            return True
        if word.lower()!=reversed_word.lower():
            return False
        


            

                
                    
                    

 


        

                