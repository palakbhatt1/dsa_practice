class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        st = []

        for i in range(len(operations)):

            if operations[i] not in ["C", "D", "+"]:
                st.append(int(operations[i]))

            elif operations[i] == "C":
                st.pop()

            elif operations[i] == "D":
                st.append(st[-1] * 2)

            elif operations[i] == "+":
                st.append(st[-1]+st[-2])

        return sum(st)

        
