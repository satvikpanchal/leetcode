class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = {}

        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        pairs = 0
        for k, v in counter.items():
            if v % 2 == 1:
                return False

        return True
