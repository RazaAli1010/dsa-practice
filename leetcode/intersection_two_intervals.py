class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        if not firstList or not secondList:
            return []
        result=[]
        i=0
        j=0
        n=len(firstList)
        m=len(secondList)
        while i<n and j<m:
            start=max(firstList[i][0],secondList[j][0])
            end=min(firstList[i][1],secondList[j][1])
            if start<=end:
                result.append([start,end])
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        return result
