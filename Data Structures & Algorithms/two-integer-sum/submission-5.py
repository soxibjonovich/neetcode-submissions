class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            sum = nums[left] + nums[right]
            print(sum)
            print(f"{left=}")
            print(f"{right=}")
            if sum == target:
                return [left, right]
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1
            
        return [0, 0]