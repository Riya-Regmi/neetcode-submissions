class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count=0
        time=[target]*len(position) #10,10
        while position!=time:
            check=[0]*len(position)
            for i in range(len(position)):
                if position[i]==target:
                    continue
                else:
                    a=position[i]+speed[i]
                    if a in position:
                        speed[i]=a
                    if a>=target:
                        position[i]=target #7,8
                        check[i]=target
                    elif a<target:
                        position[i]=a
                    
            if target in check:
                count+=1
                

        return count
            

            
            




            


        


