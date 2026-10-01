import heapq
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        available_options=[]
        count=0
        station_pointer=0
        while True:
            if startFuel>=target:
                return count
            while station_pointer<len(stations) and stations[station_pointer][0]<=startFuel:
                    

                    heapq.heappush(available_options,-stations[station_pointer][1])
                    station_pointer+=1
            if not available_options:
                return -1
            startFuel+=-(heapq.heappop(available_options))
            count+=1
        
        

