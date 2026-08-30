class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        start.sort()
        end.sort()
        room=0
        result=0
        i=0
        j=0
        n=len(start)
        while i<n:
            if start[i]<end[j]:
                room+=1
                result=max(result,room)
                i+=1
            else:
                room-=1
                j+=1
        return result
        
        
        
