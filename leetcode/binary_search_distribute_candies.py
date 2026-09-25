class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if sum(candies)<k:
            return 0
        def isValid(num):
            count=0
            for pile in candies:
                count+=pile//num
            return count>=k
        lo=1
        hi=max(candies)
        while lo<hi:
            mid=lo+(hi-lo+1)//2
            if isValid(mid):
                lo=mid
            else:
                hi=mid-1
        return lo

        