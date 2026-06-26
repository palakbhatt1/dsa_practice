class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        i  = len(nums)-1
        res=[0]* len(nums)

        while left <= right:
            if abs(nums[left])>abs(nums[right]):
                res[i] = nums[left]*nums[left]
                left +=1
            else:
                res[i] = nums[right]*nums[right]
                right -= 1
            
            i-=1
        
        return res