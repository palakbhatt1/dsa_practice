class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        w = s.split()

        if len(pattern) != len(w):
            return False

        for i in range(len(pattern)):
            for j in range(i):
                if pattern[i] == pattern[j]:
                    if w[i] != w[j]:
                        return False

                if w[i] == w[j]:
                    if pattern[i] != pattern[j]:
                        return False

        return True