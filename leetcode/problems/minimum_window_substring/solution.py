class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        freq = {}
        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        formed = 0
        required = len(need)

        min_len = float("inf")
        start = 0

        for right in range(len(s)):

            freq[s[right]] = freq.get(s[right], 0) + 1

            if s[right] in need and freq[s[right]] == need[s[right]]:
                formed += 1

            while formed == required:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                freq[s[left]] -= 1

                if s[left] in need and freq[s[left]] < need[s[left]]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]
        
    