class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        min_e = nums[0]
        max_e= nums[0]
        
        min_sum =nums[0]
        max_sum = nums[0]

        total = sum(nums)

        for i in range (1, len(nums)):

            min_e = min(nums[i], min_e + nums[i])
            max_e = max(nums[i], max_e + nums[i])

            min_sum = min(min_e, min_sum)
            max_sum = max(max_e, max_sum)

        if max_sum<0:
            return max_sum

        return max(max_sum, total - min_sum)





        

       