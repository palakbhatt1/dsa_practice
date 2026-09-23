class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        
        left = 0
        right = 0

        for left in range(len(nums)):
            if nums[left] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
            
        return nums


        


       
        