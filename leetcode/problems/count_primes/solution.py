class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0

        arr = [1] * n

        arr[0] = 0
        arr[1] = 0

        for i in range(2, int(n ** 0.5) + 1):

            if arr[i] == 1:

                for j in range(i * i, n, i):
                    arr[j] = 0

        return sum(arr)