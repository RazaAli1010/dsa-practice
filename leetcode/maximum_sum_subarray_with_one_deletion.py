class Solution(object):
    def maximumSum(self, arr):
        one_delete=float("-inf")
        no_delete=arr[0]
        result=arr[0]
        for i in range(1,len(arr)):
            one_delete=max(one_delete+arr[i],no_delete)
            no_delete=max(no_delete+arr[i],arr[i])
            result=max(result,max(no_delete,one_delete))
        return result
        