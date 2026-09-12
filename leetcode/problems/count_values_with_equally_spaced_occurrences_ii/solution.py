class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:

        a = nums
        freq = {}
        index = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1

            if nums[i] not in index:
                index[nums[i]] = []

            index[nums[i]].append(i)

        ans = 0

        for x in freq:
            if freq[x] >= 3:
                arr = index [x]
                gap = arr[1] - arr[0]                
                found = True

                for i in range (1, len(arr)-1):
                   if arr[i + 1] - arr[i] != gap:
                        found = False
                        break

                if found:
                    ans += 1
                            
        return ans
            
    
        