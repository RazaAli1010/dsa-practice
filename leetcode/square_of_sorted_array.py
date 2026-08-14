class Solution(object):
    def sortedSquares(self, nums):
        n=len(nums)
        result=[0]*n
        left=0
        right=n-1
        index=n-1
        while left<=right:
            left_squared=nums[left]**2
            right_squared=nums[right]**2
            if left_squared>right_squared:
                result[index]=left_squared
                left+=1
            else:
                result[index]=right_squared
                right-=1
            index-=1
        return result
