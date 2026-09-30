import heapq
class Solution:
    def mergeArrays(self, mat):
        # code here
        heap=[]
        result=[]
        n=len(mat[0])
        j=0
        for i in range(len(mat)):
            heapq.heappush(heap,(mat[i][j],i,j))
        while heap:
            val, index, pos=heapq.heappop(heap)
            result.append(val)
            if pos+1<n:
                heapq.heappush(heap,(mat[index][pos+1],index,pos+1))
        return result