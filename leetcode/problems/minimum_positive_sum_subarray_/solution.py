class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
    
        n = len(nums)
        ans = float("inf")

        for i in range(n):
            curr_sum = 0

            for j in range(i, n):
                curr_sum += nums[j]
                length = j - i + 1

                if l <= length <= r:
                    if curr_sum > 0:
                        ans = min(ans, curr_sum)

                if length > r:
                    break

        return ans if ans != float("inf") else -1