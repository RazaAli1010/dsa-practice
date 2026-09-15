class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def hoursNeeded(k):
            total_hours=0
            for p in piles:
                total_hours+=(p+k-1)//k
            return total_hours<=h
        lo=1
        hi=max(piles)
        while lo<hi:
            mid=lo+(hi-lo)//2
            if (hoursNeeded(mid)):
                hi=mid
            else:
                lo=mid+1
        return lo
                

        