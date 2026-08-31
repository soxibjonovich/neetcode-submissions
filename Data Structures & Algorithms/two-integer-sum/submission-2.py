class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left = 0
        right = len(nums) - 1

        while left <= right:
            sum = sorted_nums[left] + sorted_nums[right]
            if sum == target:
                return [nums.index(sorted_nums[left]), nums.index(sorted_nums[right])]
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1
        return [0, 0]