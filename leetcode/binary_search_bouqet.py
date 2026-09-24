class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m*k>len(bloomDay):
            return -1
        def daysNeeded(d):
            count=0
            flower_bloomed=0
            for days in bloomDay:
                if days<=d:
                    count+=1
                    if count==k:
                        flower_bloomed+=1
                        count=0
                else:
                    count=0
            return flower_bloomed>=m
        lo=min(bloomDay)
        hi=max(bloomDay)
        while lo<hi:
            mid=lo+(hi-lo)//2
            if daysNeeded(mid):
                hi=mid
            else:
                lo=mid+1
        return lo 

        