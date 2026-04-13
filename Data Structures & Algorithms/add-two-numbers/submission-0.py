# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = l1.val + l2.val
        carry = 0
        if sum1 > 9:
            carry = 1
            sum1 = sum1 % 10
        result = ListNode(val=sum1)
        head = result
        while(l1.next or l2.next):
            if l1.next:
                l1 = l1.next
            else:
                l1 = ListNode(val=0)
            if l2.next:
                l2 = l2.next
            else:
                l2 = ListNode(val=0)
            sum = l1.val + l2.val
            if carry == 1:
                sum += 1
                carry = 0
            if sum > 9:
                carry = 1
                sum = sum % 10
            result.next = ListNode(val=sum)
            result = result.next
        if carry > 0:
            result.next = ListNode(val=1)
            result = result.next
        return head