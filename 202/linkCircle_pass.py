'''Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getNextNum(n):
            sum = 0
            while n > 0:
                i, d = divmod(n, 10)
                n = i
                sum += d ** 2
            return sum

        slow = fast = n
        while True:
            slow = getNextNum(slow)
            fast = getNextNum(getNextNum(fast))
            if fast == 1:
                return True
            elif slow == fast:
                return False

if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))    





