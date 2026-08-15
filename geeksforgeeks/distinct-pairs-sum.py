class Solution:
    def distinctPairs(self, arr, target):
        # code here
        left=0
        right=len(arr) - 1
        arr.sort()
        result=[]
        while left<right:
            if arr[left]+arr[right]==target:
                result.append([arr[left],arr[right]])
                left+=1
                right-=1
                while left<right and arr[left]==arr[left-1]:
                    left+=1
                while left<right and arr[right]==arr[right+1]:
                    right-=1
            elif arr[left]+arr[right]>target:
                right-=1
            else:
                left+=1
        
        return result
                
        