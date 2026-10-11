class Solution:
    def maxArea(self, heights: List[int]) -> int:
        index=0
        h=0
        b=0
        area=0
        for id,height in enumerate(heights): #2,2
            if height>h: #7>2
                h=height  #7
                b=id  #1
            a=(min(h,height))*(id-b) #(2*2)
            if a>area: #4
                area=a
        return area


            




       

        





                



        



            
            

        
            


        
        