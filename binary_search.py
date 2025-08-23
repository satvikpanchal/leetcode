class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            midpoint = (l + r) // 2

            if nums[midpoint] > target:
                r = midpoint - 1
            elif nums[midpoint] < target:
                l = midpoint + 1
            else:
                return midpoint

        return -1
        