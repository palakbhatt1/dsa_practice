class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        j = 0 
        for ch in s:
            for i in range(j, len(t)):
                if t[i] == ch:
                    j = i + 1
                    break
            else :
                return False
        return True

                
           