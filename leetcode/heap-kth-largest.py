import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap=[]
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]

        