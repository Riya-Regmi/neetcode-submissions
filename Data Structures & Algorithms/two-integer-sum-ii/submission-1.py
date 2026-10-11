class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        arr=set()
        while i<len(numbers):
            diff=target-numbers[i]
            if diff in numbers and numbers[i]<diff:
                
                arr.update([i,])
                return list(arr)
            else:
                i+=1
                




            

        