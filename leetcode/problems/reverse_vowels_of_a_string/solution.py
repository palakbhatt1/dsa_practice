class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = list(s)

        x = ['a', 'e','i', 'o','u', 'A','E','I','O','U']

        left = 0
        right = len(s) - 1

        while left < right:
           
            if s[left] in x and s[right] in x:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -=1

            elif s[left] in x and s[right] not in x:
                right -= 1
            
            else:
                left += 1
                
        return "".join(s)