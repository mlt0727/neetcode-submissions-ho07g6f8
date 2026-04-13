class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        longest = 0

        for n in set1:
            if n-1 not in set1:
                length = 1
                while n + length in set1:
                    length += 1
                longest = max(longest, length)
        return longest
