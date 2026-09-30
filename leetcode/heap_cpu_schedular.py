from collections import deque, Counter
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq=Counter(tasks)
        heap=[-c for c in freq.values()]
        heapq.heapify(heap)
        timer=0
        cooldown=deque()
        while heap or cooldown:
            timer+=1
            if heap:
                cnt=heapq.heappop(heap)+1
                if cnt!=0:
                    cooldown.append((cnt,timer+n))
            if cooldown and cooldown[0][1]==timer:
                heapq.heappush(heap,cooldown.popleft()[0])
        return timer
        



        