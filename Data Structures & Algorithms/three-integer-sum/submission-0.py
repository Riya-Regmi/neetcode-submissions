

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        array=nums.sort() #-4,-1,-1,0,1,2
        i=0
        j=len(nums)-1
        k=1
        output=[]
        while i<j:
            if k!=i and k!=j and nums[k]==nums[i]+nums[j]: #-1=-1+0
                output.append([nums[i],nums[k],nums[j]])
            else:
                k+=1
            i+=1
            j-=1
        return output
                


                                
        



        
