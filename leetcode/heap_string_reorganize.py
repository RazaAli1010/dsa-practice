import heapq
from collections import Counter
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq=Counter(s)
        heap=[(-cnt,ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)

        prev=None
        result=[]
        while heap:
            cnt, ch=heapq.heappop(heap)
            result.append(ch)
            cnt+=1
            if prev:
                heapq.heappush(heap,prev)
                prev=None
            if cnt!=0:
                prev=(cnt,ch)
        return "" if prev else "".join(result)
        
        