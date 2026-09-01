class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range (len(nums)):
            if i in nums:
                pass
            else:
                 return i

        return len(nums) # if the no is greater than larger no