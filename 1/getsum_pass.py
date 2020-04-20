class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            vj = target - nums[i]
            if vj in nums:
                j = nums.index(vj)
                if i != j:
                    return [i, j]
