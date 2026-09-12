class Solution:
    def findCeil(self, arr, x):
        # code here
        lo=0
        hi=len(arr)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            if (arr[mid]>=x):
                hi=mid
            else:
                lo=mid+1
        return lo if arr[lo]>=x else -1
