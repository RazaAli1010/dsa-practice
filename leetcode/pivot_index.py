class Solution(object):
    def pivotIndex(self, nums):
        n=len(nums)
        total=sum(nums)
        for i in range(n):
            if i==0:
                left=0
            else:
                left+=nums[i-1]
            right=total-left-nums[i]
            if right==left:
                return i
            
        return -1
        