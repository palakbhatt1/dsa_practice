class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        st = []
        res = []

        for i in range(len(s)):
            st.append(s[i])
        
        while len(st) > 0:
            c = st[-1]
            st.pop()
            res.append(c)

        s[:] = res
    
