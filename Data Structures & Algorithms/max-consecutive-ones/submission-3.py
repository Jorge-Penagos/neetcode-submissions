class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutives = 0
        result = 0

        for num in nums:
            if num == 1:
                consecutives += 1
            else:
                consecutives = 0

            result = max(result, consecutives)

        return result