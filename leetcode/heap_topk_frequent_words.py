import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq={}
        for word in words:
            freq[word]=freq.get(word,0)+1
        heap=[]
        result=[]
        for key, frequency in freq.items():
            heap.append((-frequency, key))
        heapq.heapify(heap)
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

        

        