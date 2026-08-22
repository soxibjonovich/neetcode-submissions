class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                return True
            slow += 1
            fast += 1
        return False