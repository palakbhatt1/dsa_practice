class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        i =0
        j = k-1
        
        total = 0

        for x in range(k):
            total += nums[x]

        max_s = total

        while j < len(nums) - 1:

            
            i += 1
            j += 1

            total += nums[j]
            total -= nums[i-1]
            max_s = max(max_s, total)

        return max_s/k