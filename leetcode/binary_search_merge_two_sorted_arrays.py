class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        m=len(nums1)
        n=len(nums2)
        if m>n:
            nums1, nums2=nums2, nums1
            m,n=n,m
        
            
        total_left=(m+n+1)//2
        lo=0
        hi=m
        while lo<=hi:
            i=lo+(hi-lo)//2
            j=total_left-i
            if i==0:
                l1=float("-inf")
            else:
                l1=nums1[i-1]
            if j==0:
                l2=float("-inf")
            else:
                l2=nums2[j-1]
            if i==m:
                r1=float("inf")
            else:
                r1=nums1[i]
            if j==n:
                r2=float("inf")
            else:
                r2=nums2[j]
            if l1<=r2 and l2<=r1:
                if (m+n)%2==0:
                    return (max(l1,l2)+min(r1,r2))/2.0
                else:
                    return max(l1,l2)
            elif l1>r2:
                hi=i-1
            else:
                lo=i+1

        