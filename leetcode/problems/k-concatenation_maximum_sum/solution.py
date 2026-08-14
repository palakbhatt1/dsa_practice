class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        total = sum(arr)

        b_e = 0
        res = 0

        for i in range(len(arr)):
            b_e = max(0, arr[i] + b_e)
            res = max(res, b_e)

        if k == 1:
            return res % (10**9 + 7)

        curr = 0
        prefix = 0

        for i in range(len(arr)):
            curr += arr[i]
            prefix = max(prefix, curr)

        curr = 0
        suffix = 0

        for i in range(len(arr) - 1, -1, -1):
            curr += arr[i]
            suffix = max(suffix, curr)

        res = max(res, prefix + suffix)

        if total > 0:
            res = max(res, prefix + suffix + (k - 2) * total)

        return res % (10**9 + 7)