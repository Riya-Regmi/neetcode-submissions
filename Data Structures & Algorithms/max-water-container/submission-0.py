class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight=0
        width=0
        for idx,height in enumerate(heights):
            if  maxHeight<height:
                maxHeight=height
                width=idx #1
        area=maxHeight*width #7
        for idx,height in enumerate(heights):
            h=min(maxHeight,height) 
            w=idx-width
            calc=h*w
            area=max(area,calc)
        return area





                



        



            
            

        
            


        
        