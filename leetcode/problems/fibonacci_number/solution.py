class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
            
        a = 0
        b = 1

        while n>1:
            r = a + b
            a = b
            b = r
            n-=1

        return b

        