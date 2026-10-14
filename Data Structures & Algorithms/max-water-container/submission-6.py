class Solution:
    def maxArea(self, heights: List[int]) -> int:
        index=0
        h=0
        b=0
        area=0
        for id,height in enumerate(heights): #0,1
            if height>h: #2>1
                h=height  #1
                b=id      #0
            a=(min(h,height))*(id-b) #(2*2)
            if a>area: #4
                area=a
        return area


            




       

        





                



        



            
            

        
            


        
        