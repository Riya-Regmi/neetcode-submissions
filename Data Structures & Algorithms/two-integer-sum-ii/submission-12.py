class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        output=[]
        while left<len(numbers)-1:
            sum=numbers[left]+numbers[right]
            if sum==target and left<right:
                output.append(left+1)
                output.append(right+1)
                left+=1
            elif sum!=target and right>left:
                right-=1
            elif sum!=target and right==left:
                right=len(numbers)-1
                left+=1
                
        return output



        
                




            

        