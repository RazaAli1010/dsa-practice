class Solution(object):
    def subarraysDivByK(self, nums, k):
        result=0
        current_sum=0
        freq={0:1}
        for num in nums:
            current_sum+=num
            remainder=current_sum%k
            result+=freq.get(remainder,0)
            freq[remainder]=freq.get(remainder,0)+1
        return result
            
        