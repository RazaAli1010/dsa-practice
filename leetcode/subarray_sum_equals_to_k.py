class Solution(object):
    def subarraySum(self, nums, k):
        result=0
        total_sum=0
        freq={0:1}
        for num in nums:
            total_sum+=num
            diff=total_sum-k
            result+=freq.get(diff,0)
            freq[total_sum]=freq.get(total_sum,0)+1
        return result
        