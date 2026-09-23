class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        left = 1
        right = 1

        for left in range(1, len(nums)):
            if nums[left] != nums[left - 1]:
                nums[right] = nums[left]  
                right += 1      

        return right 

            

        



        
        