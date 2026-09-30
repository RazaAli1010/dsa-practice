from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq=Counter(tasks)
        frequencies=list(freq.values())
        frame=max(frequencies)
        val_count=frequencies.count(frame)
        minimum_count=(frame-1)*(n+1)+val_count
        return max(minimum_count,len(tasks))
        



        