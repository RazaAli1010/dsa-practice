import heapq
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        heap=[]
        projects = sorted(zip(capital, profits))
        num_of_projects=0
        profit_pointer=0
        while k>num_of_projects:
            while profit_pointer<len(projects) and projects[profit_pointer][0]<=w:
                heapq.heappush(heap,-projects[profit_pointer][1])
                profit_pointer+=1
            if heap:

                max_prof=-heapq.heappop(heap)
                w+=max_prof
                num_of_projects+=1
            else:
                break
        return w

        