class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        # Check each character of the first string
        for i in range(len(strs[0])):

            # Compare with every other string
            for word in strs[1:]:

                # Stop if word is shorter or character differs
                if i >= len(word) or word[i] != strs[0][i]:
                    return prefix

            # Character is common in every word
            prefix += strs[0][i]

        return prefix
        