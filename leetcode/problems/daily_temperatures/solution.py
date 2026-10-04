class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        ans = [0] * len(temperatures)

        t_st = []
        i_st = []

        for i in range(len(temperatures)):
            while t_st and temperatures[i] > t_st[-1]:

                t_st.pop()
                prev_index = i_st.pop()
                ans[prev_index] = i - prev_index

            t_st.append(temperatures[i])
            i_st.append(i)

        return ans

