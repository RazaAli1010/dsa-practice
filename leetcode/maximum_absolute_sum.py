class Solution(object):
    def maxAbsoluteSum(self, nums):
        max_sum=nums[0]
        min_sum=nums[0]
        result=abs(nums[0])
        for i in range(1,len(nums)):
            max_sum=max(nums[i],nums[i]+max_sum)
            min_sum=min(nums[i],nums[i]+min_sum)
            result=max(result,max(max_sum,abs(min_sum)))
        return result