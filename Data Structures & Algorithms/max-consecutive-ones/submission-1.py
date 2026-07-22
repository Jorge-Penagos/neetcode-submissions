class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutives = 0
        final = 0
        for i in nums:
            if i == 1:
                consecutives += 1
            else:
                if final < consecutives:
                    final = consecutives
                consecutives = 0
        if final < consecutives:
            final = consecutives
        return final