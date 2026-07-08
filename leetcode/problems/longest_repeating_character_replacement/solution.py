class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        max_len = 0
        max_freq = 0

        freq = {}

        for right in range (len(s)):
            freq[s[right]]  = freq.get(s[right], 0) + 1

            max_freq =  max(max_freq, freq[s[right]])

            win_len = right - left + 1
            diff = win_len - max_freq

            while diff > k:
                freq[s[left]] -= 1
                left += 1

                win_len = right - left + 1
                diff = win_len - max_freq

            max_len = max(max_len, win_len)

        return  max_len

