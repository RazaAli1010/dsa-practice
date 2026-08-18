class Solution(object):
    def characterReplacement(self, s, k):
        low=0
        freq={}
        n=len(s)
        result=1
        for high in range(n):
            freq[s[high]]=freq.get(s[high],0)+1
            length=high-low+1
            max_value=max(freq.values())
            diff=abs(length-max_value)
            while diff>k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
                length=high-low+1
                max_value=max(freq.values())
                diff=abs(length-max_value)
            length=high-low+1
            result=max(result,length)
        return result
        