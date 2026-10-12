class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx,num in enumerate(numbers): #0
            sum=target-num 
            if sum in numbers[idx+1:]: #[2,3,4]
                index=(numbers[idx+1:].index(sum)) + idx +1  #1+0
                output=[idx+1,index+1]
                return output
            else:
                continue


        
                




            

        