class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        i = 0
        j = i+1

        while i<j:
            for j in range(len(nums)):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                

            return nums