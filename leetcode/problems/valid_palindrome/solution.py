class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = ""

        for ch in s:
            if ch.isalnum():
                res += ch

        org = res.lower()

        if org == org[::-1]:
            return True
        else:
            return False

        

        