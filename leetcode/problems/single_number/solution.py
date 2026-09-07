class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        freq = {}

        for i in range(len(nums)):

            freq[nums[i]] = freq.get(nums[i], 0) + 1

        for i in range(len(nums)):
            if freq[nums[i]] == 1:
                return nums[i]

    

