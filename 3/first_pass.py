'''Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        win = 2
        start = 0
        length = len(s)
        while start+win <= length:
            if not Solution.has_same(s[start:start+win]):
                win += 1
            else:
                start += 1
        return win-1

    @staticmethod
    def has_same(l: list) -> bool:
        if len(l) < 2:
            return False
        if len(l) != len(set(l)):
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("bbbbbaccc"))
