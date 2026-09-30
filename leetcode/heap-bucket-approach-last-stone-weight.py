import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        
        """
        W=max(stones)
        count=[0]*(W+1)
        for stone in stones:
            count[stone]+=1
        cur=W
        while cur>0 :
            if count[cur]==0:
                cur-=1
                continue
            if count[cur]%2==0:
                count[cur]=0
                cur-=1
                continue
            nxt=cur-1
            while nxt>0 and count[nxt]==0:
                nxt-=1
            if nxt==0:
                return cur
            count[cur]=0
            count[nxt]-=1
            count[cur-nxt]+=1
            cur-=1
        return 0
            
            
        
        
        