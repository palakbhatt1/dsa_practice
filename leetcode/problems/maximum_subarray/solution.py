class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        b_e= nums[0] #best_ending
        ans= nums[0]

        for i in range(1,len(nums)):
            v1 = b_e + nums[i]
            v2 = nums[i]
            b_e = max(v1,v2)
            ans = max(ans,b_e)

        return ans