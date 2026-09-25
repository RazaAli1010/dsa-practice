class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m=len(matrix)
        n=len(matrix[0])
        lo=0
        hi=m*n-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            row, col=mid//n, mid%n
            val=matrix[row][col]
            if val==target:
                return True
            elif val>target:
                hi=mid-1
            else:
                lo=mid+1
        return False