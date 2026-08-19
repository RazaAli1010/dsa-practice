class Solution(object):
    def checkInclusion(self, s1, s2):
        need={}
        have={}
        low=0
        for char in s1:
            need[char]=need.get(char,0)+1
        found=0
        for high in range(len(s2)):
            if s2[high] in need:
                have[s2[high]]=have.get(s2[high],0)+1
                if have[s2[high]]==need[s2[high]]:
                    found+=1
            while found==len(need):
                length=high-low+1
                if length==len(s1):
                    return True
                if s2[low] in need:
                    have[s2[low]]-=1
                    if have[s2[low]]<need[s2[low]]:
                        found-=1
                low+=1
        return False
        