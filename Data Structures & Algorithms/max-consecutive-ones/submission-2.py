class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutives = result = 0
        for i in nums:
            if i == 1:
                consecutives += 1
            else:
                if result < consecutives:
                    result = consecutives
                consecutives = 0
        if result < consecutives:
            result = consecutives
        return result