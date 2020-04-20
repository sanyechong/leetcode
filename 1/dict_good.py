class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} 
        for i in range(len(nums)):
            vj = target - nums[i]
            if vj in d.keys():
                return [i, d[vj]]
            d[nums[i]] = i
