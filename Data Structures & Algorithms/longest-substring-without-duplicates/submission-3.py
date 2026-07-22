class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        seen = {}
        leftpointer = 0
        result = 0

        for rightpointer in range(len(string)):
            if string[rightpointer] in seen:
                leftpointer = max(seen[string[rightpointer]] + 1, leftpointer)
            seen[string[rightpointer]] = rightpointer
            result = max(result, rightpointer - leftpointer + 1)
        return result