class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        v = ['a','e','i','o','u']

        low = 0
        high = k -1

        count = 0

        for i in range (high + 1):
            if s [i] in v :
                count += 1

        max_v = count

        while high < len(s) - 1:
            if s [low] in v:
                count -= 1
            
            low += 1
            high += 1

            if s [high] in v:
                count += 1

            max_v = max(max_v, count)
        return max_v
            



