import heapq
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses_sorted=sorted(courses,key=lambda course: course[1])
        total_time=0
        heap=[]
        for course in courses_sorted:
            total_time+=course[0]
            heapq.heappush(heap,-course[0])
            if total_time>course[1]:
                total_time+=heapq.heappop(heap)
        return len(heap) 

        
        