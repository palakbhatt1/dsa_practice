class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        i = 0
        j = 0
        m_prof = 0

        for i in range (len(prices)):
            if prices[i] > prices[j]:
                prof = prices[i] - prices[j]
                m_prof = max(prof, m_prof)

            else:
                j = i
                
        return m_prof
