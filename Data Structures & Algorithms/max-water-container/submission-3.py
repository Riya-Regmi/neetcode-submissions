class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        maxHeight=0
        id=0
        for idx,h in enumerate(heights):
            if h>maxHeight:
                maxHeight=h
                id=idx
        for idx,h in enumerate(heights):
            length=min(maxHeight,h)
            breadth=idx-id
            calc=length*breadth
            if calc>area:
                area=calc
        return area


        





                



        



            
            

        
            


        
        