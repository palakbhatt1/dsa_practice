class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1

        for j in range(1, len(nums)):
            if nums[j]==nums[j-1]:
                j+=1
                
            
            else:
                nums[i+1]=nums[j]
                i+=1

        return i+1
        return nums