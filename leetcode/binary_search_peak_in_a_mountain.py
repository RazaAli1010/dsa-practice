class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lo=0
        hi=len(arr)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1] or arr[mid]>arr[mid+1]:
                hi=mid
            else:
                lo=mid+1
        return lo
                
        