class Solution:
    def translateNum(self, num: int) -> int:
        numStr = str(num)
        length = len(numStr)
        if length == 1:
            return 1
        dp = 0  
        dp_first = 1
        dp_second = 1
        for i in range(2, length+1):
            strSum = int(numStr[i-2] + numStr[i-1])
            if strSum <= 25 and strSum >= 10:
                dp = dp_second + dp_first
            else:
                dp = dp_second 
            dp_first = dp_second
            dp_second = dp
        return dp
