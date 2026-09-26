class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def countLess(middle):
            count=0
            row=m
            col=1
            while row>=1 and col<=n:
                val=row*col
                if val<=middle:
                    count+=row
                    col+=1
                else:
                    row-=1
            return count
        lo=1
        hi=m*n
        while lo<hi:
            mid=lo+(hi-lo)//2
            if countLess(mid)>=k:
                hi=mid
            else:
                lo=mid+1
        return lo
        