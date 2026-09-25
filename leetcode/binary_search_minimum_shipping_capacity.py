class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canShip(cap):
            days_count=1
            current_weight=0
            for weight in weights:
                if current_weight+weight<=cap:
                    current_weight+=weight
                else:
                    days_count+=1
                    current_weight=0
                    current_weight+=weight
            return days_count<=days
        lo=max(weights)
        hi=sum(weights)
        while lo<hi:
            mid=lo+(hi-lo)//2
            if canShip(mid):
                hi=mid
            else:
                lo=mid+1
        return lo
                

        