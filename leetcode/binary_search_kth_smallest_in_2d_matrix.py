class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m=len(matrix)
        n=len(matrix[0])
        def countLess(middle):
            count=0
            row=m-1
            col=0
            while row>=0 and col<n:
                val=matrix[row][col]
                if val<=middle:
                    count+=row+1
                    col+=1
                else:
                    row-=1
            return count
        lo=matrix[0][0]
        hi=matrix[-1][-1]
        while lo<hi:
            mid=lo+(hi-lo)//2
            if countLess(mid)>=k:
                hi=mid
            else:
                lo=mid+1
        return lo
                
        