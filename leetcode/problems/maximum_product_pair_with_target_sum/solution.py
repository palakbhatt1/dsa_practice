class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:

        max_prod = float('-inf')

        res = [-1,-1]

        for j in range(len(nums)):
            for i in range (len(nums)):

                if nums[i] + nums[j] == target and nums[i] > nums[j]:

                    prod = nums[i] * nums[j] 

                    if prod > max_prod:
                        max_prod = prod
                        res = [i,j]

        return res