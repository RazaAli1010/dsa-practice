class Solution(object):
    def findMaxLength(self, nums):
        freq={}
        result=0
        count_zero=0
        count_one=0
        for i in range(len(nums)):
            if nums[i]==0:
                count_zero+=1
            else:
                count_one+=1
            diff=count_zero-count_one
            if diff==0:
                result=max(result,i+1)
            elif diff in freq:
                result=max(result,i-freq[diff])
            else:
                freq[diff]=i
        return result

        