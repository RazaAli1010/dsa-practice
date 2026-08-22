class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        best=arr[0]
        result=arr[0]
        for i in range(1,len(arr)):
            if arr[i]+best<best:
                best=arr[i]+best
            else:
                best=arr[i]
            result=min(result,best)
        return result