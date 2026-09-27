import bisect

class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums2)

        def countLessEqual(P):
            count = 0
            for x in nums1:
                if x == 0:
                    if P >= 0:
                        count += n
                elif x > 0:
                    threshold = P // x
                    count += bisect.bisect_right(nums2, threshold)
                else:
                    threshold = -((-P) // x)
                    count += n - bisect.bisect_left(nums2, threshold)
            return count

        lo = min(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])
        hi = max(nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1])

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if countLessEqual(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo