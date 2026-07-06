class Solution:
    def longestKSubstr(self, s, k):
        
        max_len = -1
        
        for i in range(len(s)):
            
            freq = {}
            
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0)+1
                
                if len(freq)==k:
                    max_len = max(max_len, j-i+1)
                    
                elif len(freq)>k:
                    break
        
        return max_len
        
        
