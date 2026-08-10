class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        min_e = nums[0]
        max_e = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):

            v1 = nums[i]
            v2 = nums[i] * min_e
            v3 = nums[i] * max_e
            min_e = min(v1,min(v2,v3))
            max_e = max(v1,max(v2,v3))
            res = max(res,max(max_e,min_e))
            
        return res

