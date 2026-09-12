class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        
        freq = {}
        index = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1

            if nums[i] not in index:
                index[nums[i]] = []

            index[nums[i]].append(i)

        ans = 0

        for x in freq:
            if freq[x] == 3:
                if index[x][1] - index[x][0] == index[x][2] - index[x][1]:
                    ans += 1

        return ans
            
    