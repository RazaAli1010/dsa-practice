class Solution(object):
    def findMaxAverage(self, nums, k):
        n=len(nums)
        window_sum=sum(nums[:k])
        window_average=float(window_sum)/k
        max_average=window_average
        for i in range(k,n):
            window_sum+=nums[i]-nums[i-k]
            window_average=float(window_sum)/k
            max_average=max(max_average,window_average)
        return max_average
        