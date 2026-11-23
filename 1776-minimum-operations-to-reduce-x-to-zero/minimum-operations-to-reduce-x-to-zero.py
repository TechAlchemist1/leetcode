class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        prefixMap = {0: -1}
        prefix = 0
        total = sum(nums)
        longest = 0 if total == x else -1

        for i in range(len(nums)):
            prefix += nums[i]

            if prefix - (total - x) in prefixMap:
                index = prefixMap[prefix - (total - x)]
                longest = max(longest, i - index)

            prefixMap[prefix] = i

        if longest == -1:
            return -1

        size = len(nums) - longest
        return size