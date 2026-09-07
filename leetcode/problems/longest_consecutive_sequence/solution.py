class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        nums.sort()

        curr = 1
        longest = 1

        for i in range(len(nums)-1):

            if nums[i+1] == nums[i] + 1:
                curr += 1
            
            elif nums[i+1] == nums[i]:
                continue
            
            else:
                curr = 1
            
            longest = max(curr, longest)
        
        return longest
            
        






        
