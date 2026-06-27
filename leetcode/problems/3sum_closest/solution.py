class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        max_diff = float("inf")

        for i in range (len(nums)-2):

            left = i+1
            right = len(nums)-1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum -  target) 

                if max_diff > diff :
                    max_diff = diff
                    res_sum = sum

                if sum == target:
                    return sum

                elif sum < target:
                    left += 1

                else: 
                    right -= 1
        
        return res_sum