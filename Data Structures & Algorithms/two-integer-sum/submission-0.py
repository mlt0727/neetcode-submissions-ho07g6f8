class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of = {}  # 值 -> 下标 的哈希表
        for i, x in enumerate(nums):
            y = target - x
            if y in index_of:          # 找到配对
                return [index_of[y], i]
            index_of[x] = i            # 记录当前值的位置