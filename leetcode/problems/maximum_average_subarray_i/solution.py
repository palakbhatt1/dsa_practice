class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        low = 0
        high = k - 1

        total = 0

        for i in range (high +1):
            total += nums[i]

        max_s = total

        while high < len(nums) - 1:
            total += nums[high+1] - nums[low]
            low += 1
            high += 1

            max_s = max (max_s, total)

        return max_s/k

    