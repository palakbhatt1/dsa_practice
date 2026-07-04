class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        low = 0
        high = 0
        total = 0
        res =  float('inf')

        while high < len(nums):
            total += nums[high]

            while total >= target:

                length = high -low + 1
                res = min(res, length)
                total -= nums[low]
                low +=1
        
            high +=1

        if res == float('inf'):
            return 0

        return res
    
