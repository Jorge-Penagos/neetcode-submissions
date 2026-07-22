class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = sorted(nums)
        return res[0]