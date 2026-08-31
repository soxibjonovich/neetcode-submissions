class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = sorted((v, i) for i, v in enumerate(nums))
        left, right = 0, len(nums) - 1
        while left < right:
            s = indexed[left][0] + indexed[right][0]
            if s == target:
                return sorted([indexed[left][1], indexed[right][1]])
            elif s > target:
                right -= 1
            else:
                left += 1
        return [0, 0]
