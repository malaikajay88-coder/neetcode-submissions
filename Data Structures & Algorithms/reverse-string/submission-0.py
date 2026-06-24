class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            # Swap characters
            s[left], s[right] = s[right], s[left]

            # Move pointers inward
            left += 1
            right -= 1
        