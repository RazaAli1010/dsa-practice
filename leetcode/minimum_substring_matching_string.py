class Solution(object):
    def minWindow(self, s, t):
        low=0
        freq_t={}
        freq_s={}
        m=len(s)
        for charactor in t:
            freq_t[charactor]=freq_t.get(charactor,0)+1
        formed=0
        min_length=float("inf")
        result=""
        for high in range(m):
            if s[high] in freq_t:
                freq_s[s[high]]=freq_s.get(s[high],0)+1
                if freq_s[s[high]]==freq_t[s[high]]:
                    formed+=1
            while formed==len(freq_t):
                length=high-low+1
                if length<min_length:
                    min_length=length
                    result=s[low:high+1]

                
                if s[low] in freq_s:
                    freq_s[s[low]]-=1
                    if freq_s[s[low]]<freq_t[s[low]]:
                        formed-=1
                low+=1
        return result
            

            

        