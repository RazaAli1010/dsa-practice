class Solution(object):
    def insert(self, intervals, newInterval):
        merged=[]
        i,n=0,len(intervals)
        start,end=newInterval[0],newInterval[1]
        while i<n and intervals[i][1]< start:
            merged.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=end:
            start=min(start,intervals[i][0])
            end=max(end,intervals[i][1])
            i+=1
        merged.append([start,end])
        while i<n:
            merged.append(intervals[i])
            i+=1
        return merged
        


            


            


            


        