class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        max_e = nums[0]
        min_e = nums[0]
        ans = abs(nums[0])

        for i in range (1, len(nums)):

            v1 = nums[i]
            v2 = nums[i]+ max_e
            v3 = nums[i]+ min_e

            max_e = max(v1,v2,v3)
            min_e = min(v1,v2,v3)
            ans = max(abs(max_e),abs(min_e), ans)

        return ans