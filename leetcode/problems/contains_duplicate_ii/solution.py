class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        last_index = {}

        for i in range (len(nums)):
            if nums[i] in last_index:
                diff = i - last_index[nums[i]]

                if diff<=k:
                    return True

            last_index[nums[i]] = i

        return False




            