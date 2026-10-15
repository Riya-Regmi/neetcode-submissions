class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count=0
        time=[1]*len(position)
        for i in range(len(position)):
            t=(target-position[i])/speed[i]
            time[i]=int(t)
        seen={}
        for i in time: #3,4.5,10,3
            if i not in seen:#3:1
                seen[i]=0
                count+=1
            seen[i]+=1
        return count



            


        


