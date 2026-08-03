class Solution:
    def squareSum(self, n):

        total = 0

        while n > 0:
            d = n % 10
            n = n//10
            total += d*d

        return total

    def isHappy(self, n: int) -> bool:

        slow = n
        fast = n

        while fast!= 1:
            slow = self.squareSum(slow)
            fast = self.squareSum(fast)
            fast = self.squareSum(fast)

            if slow == fast and slow != 1:
                return False
            

        return True
        