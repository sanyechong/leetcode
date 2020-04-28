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
            if nums[begin] < nums[mid]:
                if target < nums[mid] and target > nums[begin]:
                    return self.search_s(nums[begin:mid], target)
                else:
                    return self.search(nums[mid+1:last+1], target)
            else:
                if target < nums[last] and target > nums[mid]:
                    return self.search_s(nums[mid+1:last+1], target)
                else:
                    return self.search(nums[begin:mid], target)

    def search_s(self, nums, target) -> int:
        begin = 0
        last = len(nums) - 1
        if last < 0:
            return -1
        elif last == 0:
            return 0 if target == nums[last] else -1
        if target < nums[begin] or target > nums[last]:
            return -1
        while begin <= last:
            mid = (begin+last) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                begin = mid
            else:
                last = mid


if __name__ == '__main__':
    num = [2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 16, 18, 19, 25, 28, 39, 41, 0, 1]
    num_s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 18
    s = Solution()
    print(s.search(num, target))