class Solution(object):
    def maxSubArray(self, nums):
        best=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            if nums[i]+best>nums[i]:
                best=nums[i]+best
            else:
                best=nums[i]
            result=max(result,best)
        return result
        