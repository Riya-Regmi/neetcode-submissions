class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        arr=set()
        while i<len(numbers):
            diff=target-numbers[i]
            if diff in numbers:
                index=numbers.index(diff)
                arr.update([i+1,index+1])
                return list(sorted(arr))
            else:
                i+=1
                




            

        