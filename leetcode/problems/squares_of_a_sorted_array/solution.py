class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        for i in range(0, len(nums)):
            nums[i]= nums[i]*nums[i]

        nums.sort()

        return nums