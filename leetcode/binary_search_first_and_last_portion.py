class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        
        lo, hi=0, len(nums)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            if nums[mid]>=target:
                hi=mid
            else:
                lo=mid+1
        if nums[lo]!=target:
            return [-1,-1]
        first=lo
        lo, hi=0, len(nums)-1
        while lo<hi:
            mid=lo+(hi-lo+1)//2
            if nums[mid]<=target:
                lo=mid
            else:
                hi=mid-1
        last=lo
        return[first,last]
        