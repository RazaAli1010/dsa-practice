class Solution:
    def findPages(self, arr, k):
        # code here
        if len(arr)<k:
            return -1
        def canAssign(pages):
            page_count=0
            count_student=1
            for page in arr:
                if page_count+page<=pages:
                    page_count+=page
                else:
                    count_student+=1
                    page_count=0
                    page_count+=page
            return count_student<=k
        lo=max(arr)
        hi=sum(arr)
        while lo<hi:
            mid=lo+(hi-lo)//2
            if canAssign(mid):
                hi=mid
            else:
                lo=mid+1
        return lo
                
                    
