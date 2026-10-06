class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:

        stone1 = stones.copy()

        while len(stone1) > 1:
            stone1.sort()

            y = len(stone1) - 1
            x = y - 1

            if stone1[x] == stone1[y]:

                stone1.remove(stone1[y])
                stone1.remove(stone1[x])


            else:

                stone1[y] = stone1[y] - stone1[x]
                stone1.remove(stone1[x])
                
        if len(stone1) > 0:
            return stone1[0]
        
        else:
            return 0
        