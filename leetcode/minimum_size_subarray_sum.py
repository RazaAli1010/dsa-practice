class Solution(object):
    def minSubArrayLen(self, target, nums):
        low=0
        result=float("inf")
        total=0
        for high in range(len(nums)):
            total+=nums[high]
            while total>=target:
                length=high-low+1
                result=min(result,total)
                total-=nums[low]
                low+=1
        if result==float("inf"):
            return 0
        return result
        