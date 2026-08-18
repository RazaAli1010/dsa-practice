class Solution(object):
    def totalFruit(self, fruits):
        freq={}
        low=0
        n=len(fruits)
        result=float("-inf")
        for high in range(n):
            freq[fruits[high]]=freq.get(fruits[high],0)+1
            if len(freq)<=2:
                total=0
                for item in freq.values():
                    total+=item
                result=max(result,total)
            else:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1
        return result