class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        array=[0]*n
        stack=[]
        for day in range(len(temperatures)):
            while stack and temperatures[day]>temperatures[stack[-1]]:
                prev_index=stack.pop()
                array[prev_index]=day-prev_index
            stack.append(day)
        return array
            
        