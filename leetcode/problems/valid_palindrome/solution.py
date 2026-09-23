class Solution:
    def isPalindrome(self, s: str) -> bool:

        s1 = []

        for ch in s.lower():
            if ch.isalnum():
                s1.append(ch)

        org = s1.copy()

        left = 0
        right = len(s1) - 1

        while left < right:
            s1[left], s1[right] = s1[right],s1[left]
            left += 1
            right -= 1
        
        rev = s1

        if rev == org:
            return True

        else:
            return False





