class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result=[]
        n=len(nums)
        i=0
        while i < n-2:
            left=i+1
            right=n-1
            target=-1*nums[i]
            while left<right:
                if nums[left]+nums[right]==target:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif nums[left]+nums[right]>target:
                    right-=1
                else:
                    left+=1
            i+=1
            while i<n-2 and nums[i]==nums[i-1]:
                i+=1
        return result

        