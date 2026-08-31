class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums)
        max_n = 0
        for n in sorted_list:
            if max_n == n:
                return True
            elif max_n < n:
                max_n = n
        return False
        