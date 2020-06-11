class Solution:
    def translateNum(self, num: int) -> int:
        numStr = str(num)
        length = len(numStr)
        if length == 1:
            return 1
        dp = [0] * (length+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, length+1):
            strSum = int(numStr[i-2] + numStr[i-1])
            if strSum <= 25 and strSum >= 10:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.translateNum(12258))
