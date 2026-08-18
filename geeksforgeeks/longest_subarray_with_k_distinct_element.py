class Solution:
    def longestKSubstr(self, s, k):
        frequency={}
        n=len(s)
        low=0
        result=float("-inf")
        for high in range(n):
            frequency[s[high]]=frequency.get(s[high],0)+1
            while len(frequency)>k:
                frequency[s[low]]-=1
                if frequency[s[low]]==0:
                    del frequency[s[low]]
                low+=1
            if len(frequency)==k:
                length=high-low+1
                result=max(result,length)
        if result==float("-inf"):
            return -1
        return result
            
            
        