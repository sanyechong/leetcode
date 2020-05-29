class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if (sum == k):
                    count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1,2,3,-1,-4,2,1,5,7,2,3,12,4,12,3,-123,183,-23,4], 2))
