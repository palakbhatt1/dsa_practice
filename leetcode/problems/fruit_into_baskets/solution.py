class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        max_len = -1
        freq = {}
        k = 2

        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1

            while len(freq) > k:
                freq[fruits[left]] -= 1

                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]


                left+=1

            if len(freq) == k or len(freq) < k:
                max_len = max(max_len, right - left + 1)

        return max_len
