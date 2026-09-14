class Solution:
    def findKRotation(self, arr):
        # code here
        lo=0
        hi=len(arr)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            if arr[mid]<=arr[hi]:
                hi=mid
            else:
                lo=mid+1
        return lo