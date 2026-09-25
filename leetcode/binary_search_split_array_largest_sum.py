class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canSplit(val):
            total_sum=0
            no_of_splits=1
            for num in nums:
                if total_sum+num<=val:
                    total_sum+=num
                else:
                    no_of_splits+=1
                    total_sum=num
            return no_of_splits<=k
        lo=max(nums)
        hi=sum(nums)
        while lo<hi:
            mid=lo+(hi-lo)//2
            if canSplit(mid):
                hi=mid
            else:
                lo=mid+1
        return lo

        