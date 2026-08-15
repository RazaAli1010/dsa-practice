class Solution(object):
    def threeSumClosest(self, nums, target):
        min_diff=float('inf')
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==target:
                    return total
                elif total>target:
                    diff=total-target
                    if diff<min_diff:
                        min_diff=diff
                        result=total
                    right-=1
                else:
                    diff=target-total
                    if diff<min_diff:
                        min_diff=diff
                        result=total
                    left+=1
        return result
                
        
                    
        
        