class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        ans = ""

        while columnNumber > 0:
            columnNumber -= 1

            r = columnNumber % 26
            ans += chr( 65 + r)

            columnNumber //= 26

        return ans[::-1]
        