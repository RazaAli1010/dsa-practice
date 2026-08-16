class Solution(object):
    def minSubArrayLen(self, target, nums):
        low,high=0,0
        n=len(nums)
        total=0
        result=float('inf')
        while high<n:
            total+=nums[high]
            while total>=target:
                length=high-low+1
                result=min(result,length)
                total-=nums[low]
                low+=1
            high+=1
        if result==float('inf'):
            return 0
        return result