class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        max_len = 0
        z_counts = 0

        for right in range (len(nums)):

            if nums[right] == 0:
                z_counts += 1
            

            while z_counts > k:

                if nums[left] == 0:
                    z_counts -= 1
                
                left +=1
            
            max_len = max(max_len, right - left + 1)
    
        return max_len