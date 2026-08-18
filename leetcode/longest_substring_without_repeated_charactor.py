class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq={}
        low=0
        n=len(s)
        result=0
        for high in range(n):
            freq[s[high]]=freq.get(s[high],0)+1
            while len(freq)<(high-low+1):
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
            length=high-low+1
            result=max(result,length)
        return result
        
