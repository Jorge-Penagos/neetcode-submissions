class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        best = 0
        for i in nums:
            if i - 1 not in seen:
                curr = i
                length = 1
                while curr + 1 in seen:
                    curr += 1
                    length += 1
                best = max(best, length)
        return best