class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        length = len(nums)
        for i in range(length):
            for j in range(i, length):
                if nums[i] + nums[j] == target and i != j:
                    res.append(i)
                    res.append(j)
        return res
