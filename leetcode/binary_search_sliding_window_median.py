import bisect
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window=sorted(nums[:k])
        result=[]
        def get_median():
            if k%2==1:
                return float(window[k//2])
            return (window[k//2-1]+window[k//2])/2.0
        result.append(get_median())
        for i in range(k,len(nums)):
            index=bisect.bisect_left(window,nums[i-k])
            window.pop(index)
            bisect.insort(window,nums[i])
            result.append(get_median())
        return result


            

        
        
            


        