class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        empty_list = []
        final_rm = rm_val = 0
        for num in nums:
            if num == val:
                rm_val += 1
            else:
                empty_list.append(num)
                final_rm += 1
        
        nums[:len(empty_list)] = empty_list
        return final_rm