class Solution:
    def squareSum(self, n):

        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        return total

    def isHappy(self, n: int) -> bool:

        slow = n
        fast = n

        while True:
            slow = self.squareSum(slow)
            fast = self.squareSum(self.squareSum(fast))

            if slow == fast:
                break

        return slow == 1