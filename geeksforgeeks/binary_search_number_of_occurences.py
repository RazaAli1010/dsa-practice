class Solution:
    def countFreq(self, arr, target):
        # code here
        lo, hi=0, len(arr)-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            if arr[mid]>=target:
                hi=mid
            else:
                lo=mid+1
        if arr[lo]!=target:
            return 0
        first=lo
        lo, hi=0, len(arr)-1
        while lo<hi:
            mid=lo+(hi-lo+1)//2
            if arr[mid]<=target:
                lo=mid
            else:
                hi=mid-1
        last=lo
        return last-first+1
        
                