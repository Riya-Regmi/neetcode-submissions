class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)+1
        while left<right: #0
            sum=target-numbers[left]
            if sum in numbers[left+1:]: #[2,3,4]
                index=(numbers[left+1:].index(sum)) + left + 1  #1+0
                output=[left+1,index+1]
                return output
            else:
                left+=1


        
                




            

        