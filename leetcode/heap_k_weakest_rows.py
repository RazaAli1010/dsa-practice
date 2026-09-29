import heapq
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def countOne(arr):
            lo=0
            hi=len(arr)
            while lo<hi:
                mid=lo+(hi-lo)//2
                if arr[mid]==0:
                    hi=mid
                else:
                    lo=mid+1
            return lo
            
        heap=[]
        for i in range(len(mat)):
            count=countOne(mat[i])
            heap.append((count,i))
        heapq.heapify(heap)
        result=[]
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
        