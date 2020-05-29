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
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if sum(nums[i:j]) == k:
                    count += 1
        return count



if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1,2,3,-1,-4,2,1,5], 2))
