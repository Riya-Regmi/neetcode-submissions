class Solution:
    def maxArea(self, heights: List[int]) -> int:
        width=len(heights)-1
        length=heights[width]
        area=0
        for idx, h in enumerate(heights):
            l=min(h,length)
            b=width-idx
            calc=l*b
            if calc>area:
                area=calc
        return area




       

        





                



        



            
            

        
            


        
        