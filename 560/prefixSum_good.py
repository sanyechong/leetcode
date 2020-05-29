'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

'''

class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        length = len(nums)
        if (length == 0):
            return 0
        prefixMap = {0:1}
        prefixSum = 0
        count = 0
        for i in range(length):
            prefixSum += nums[i]
            if (prefixSum-k in prefixMap):  #  sum(i...j) = prefixSum(j) - prefixSum(i-1) = k, so prefixSum(j) - k = prefixSum(i-1)
                count += prefixMap[prefixSum-k]
            if (prefixSum in prefixMap):
                prefixMap[prefixSum] += 1
            else:
                prefixMap[prefixSum] = 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1,2,3,-1,-4,2,1,5,7,2,3,12,4,12,3,-123,183,-23,4], 2))
