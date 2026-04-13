class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1 = {}
        for index,num in enumerate(nums):
            if num in map1:
                return True
            map1[num] = index
        return False