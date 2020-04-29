'''Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

'''
key： 我们能够根据有序的那部分判断出 target 在不在这个部分
'''

class Solution:
    def search(self, nums, target) -> int:
        begin = 0
        last = len(nums) - 1
        if last < 0:
            return -1
        elif last == 0:
            return 0 if target == nums[last] else -1
        while begin <= last:
            mid = (begin+last) // 2
            if nums[mid] == target:
                return mid
            elif nums[begin] == target:
                return begin
            elif nums[last] == target:
                return last
            if nums[begin] <= nums[mid]:
                if target < nums[mid] and target > nums[begin]:
                    last = mid - 1
                else:
                    begin = mid + 1
            else:
                if target < nums[last] and target > nums[mid]:
                    begin = mid + 1
                else:
                    last = mid - 1
        return -1


if __name__ == '__main__':
    num = [2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 16, 18, 19, 25, 28, 39, 41, 0, 1]
    num_s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 7
    s = Solution()
    print(s.search(num, target))
