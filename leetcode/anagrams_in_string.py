class Solution(object):
    def findAnagrams(self, s, p):
        result=[]
        need={}
        have={}
        for char in p:
            need[char]=need.get(char,0)+1
        low=0
        found=0
        for high in range(len(s)):
            if s[high] in need:
                have[s[high]]=have.get(s[high],0)+1
                if have[s[high]]==need[s[high]]:
                    found+=1
            while found==len(need):
                length=high-low+1
                if length==len(p):
                    result.append(low)
                if s[low] in need:
                    have[s[low]]-=1
                    if have[s[low]]<need[s[low]]:
                        found-=1
                low+=1
        return result

        