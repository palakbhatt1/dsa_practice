class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        low = 0
        high = k - 1

        total = 0
        count = 0

        for i in range (high + 1):
            total += arr[i]

        if total >= threshold * k:
            count += 1


        while high < len(arr)-1:
            total += arr[high+1] - arr[low]

            low += 1
            high += 1

            if total >= threshold * k:
                count += 1

        return count



