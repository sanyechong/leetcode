# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#        if l1.val == 0 or l2.val == 0:
#            return l1 if l1.val else l2
        sum = Solution.get_num(l1) + Solution.get_num(l2)
        l_sum = Solution.set_num(sum)
        return l_sum


    @staticmethod
    def get_num(l: ListNode):
        stack = []
        num = 0
        stack.append(l.val)
        while l.next:
            l = l.next
            stack.append(l.val)
        while stack:
            num = num*10 + stack.pop()
        return num

    @staticmethod
    def set_num( num: int) -> ListNode:
        root = ListNode(num%10)
        num = num // 10
        l = root
        while num:
            l.next = ListNode(num%10)
            l = l.next
            num = num // 10
        return root


if __name__ == '__main__':
    s = Solution()
    l1 = Solution.set_num(243)
    l2 = Solution.set_num(564)
    result = s.addTwoNumbers(l1, l2)
    print(Solution.get_num(result))




