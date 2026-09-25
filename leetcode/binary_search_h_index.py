class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n=len(citations)
        def isValid(num):
            lo=0
            hi=n-1
            while lo<hi:
                mid=lo+(hi-lo)//2
                if citations[mid]>=num:
                    hi=mid
                else:
                    lo=mid+1
            return n-lo>=num
        lo=1
        hi=n
        while lo<hi:
            mid=lo+(hi-lo+1)//2
            if isValid(mid):
                lo=mid
            else:
                hi=mid-1
        return lo



        