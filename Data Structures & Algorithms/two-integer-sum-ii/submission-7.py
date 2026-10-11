class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr=set()
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if diff in numbers:
                index=numbers.index(diff)
                arr.add(i+1)
                arr.add(index+1)
                return list(arr)
            else:
                continue
                




            

        