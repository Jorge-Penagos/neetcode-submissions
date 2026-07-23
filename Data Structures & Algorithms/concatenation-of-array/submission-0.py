class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums

        for num in range(len(nums)):
            ans.append(nums[num])
        return ans