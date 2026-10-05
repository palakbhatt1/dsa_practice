class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        st = [0]

        for i in s:

            if i == "(":
                st.append(0)

            else:
                inside = st.pop()

                if inside == 0:
                    value = 1
                else:
                    value = 2 * inside

                if st:
                    st[-1] += value
                else:
                    st.append(value)

        return st[0]