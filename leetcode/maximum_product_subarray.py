class Solution(object):
    def maxProduct(self, nums):
        best=nums[0]
        worse=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=nums[i]*best
            v3=nums[i]*worse
            best=max(v1,max(v2,v3))
            worse=min(v1,min(v2,v3))


            
            result=max(result,max(best,worse))
        return result

        