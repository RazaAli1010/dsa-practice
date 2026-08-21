class Solution(object):
    def isHappy(self, n):
        def sum_of_digit(num):
            total=0
            while num>0:
                digit=num%10
                num=num/10
                total+=digit**2
            return total
        slow=n
        fast=n
        while fast!=1:
            slow=sum_of_digit(slow)
            fast=sum_of_digit(fast)
            fast=sum_of_digit(fast)
            if slow==fast and slow!=1:
                return False
        return True

            
        