class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo=0
        hi=len(nums)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            if nums[mid]>nums[hi]:
                if nums[lo]<=target<=nums[mid]:
                    hi=mid
                else:
                    lo=mid+1
            else:
                if target>nums[mid] and target<=nums[hi]:
                    lo=mid+1
                else:
                    hi=mid
            
                
        return lo if nums[lo]==target else -1
        