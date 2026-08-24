class Solution(object):
    def maxSubarraySumCircular(self, nums):
        best_max=nums[0]
        best_min=nums[0]
        best_final=nums[0]
        worse_final=nums[0]
        total_sum=sum(nums)
        for i in range(1,len(nums)):
            best_max=max(nums[i],nums[i]+best_max)
            best_min=min(nums[i],nums[i]+best_min)
            best_final=max(best_final,best_max)
            worse_final=min(worse_final,best_min)
        if total_sum==worse_final:
            return best_final
        
        best_max_circular=total_sum-worse_final       
        result=max(best_final,best_max_circular)
        return result
            
        