class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        arr.sort()
        
        def canArrange(d):
            cows=1
            last=arr[0]
            for x in arr:
                if x-last>=d:
                    cows+=1
                    last=x
                    if cows>=k:
                        return True
            return cows>=k
        lo, hi=1, arr[-1]-arr[0]
        while lo<hi:
            mid=lo+(hi-lo+1)//2
            if canArrange(mid):
                lo=mid
            else:
                hi=mid-1
        return lo