class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for i in range(len(strs)):
            word = strs [i]
            freq = {}

            for j in range(len(word)):
                char = word[j]
                freq[char] = freq.get(char, 0) + 1

            key = str(sorted(freq.items()))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
        