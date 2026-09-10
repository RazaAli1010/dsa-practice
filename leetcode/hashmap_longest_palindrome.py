from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        count=0
        found_odd=False
        freq=Counter(s)
        
        for key in freq:
            count_in=freq[key]
            if count_in%2==0:
                count+=count_in
            else:
                count+=count_in-1
                found_odd=True

        return count+1 if found_odd else count

        