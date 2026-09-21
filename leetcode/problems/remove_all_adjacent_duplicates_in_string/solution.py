class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        st = []
        st.append(s[0])

        for i in range(1, len(s)):
            if st and st[-1] == s[i]:
                st.pop()

            else:
                st.append(s[i])

        return "".join(st)
