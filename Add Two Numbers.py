# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes 
# contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        s, carry = ListNode(), 0
        temp = s

        # Go through l1 and l2 and add the numbers up
        while l1 != None or l2 != None:
            val = 0
            if l1 == None:
                # Add up rest of l2
                val = (l2.val + carry)
                temp.next = ListNode(val % 10)
                temp = temp.next
                l2 = l2.next
            elif l2 == None:
                # Add up rest of l1
                val = (l1.val + carry)
                temp.next = ListNode(val % 10)
                temp = temp.next
                l1 = l1.next
            else:
                val = (l1.val + l2.val + carry)
                temp.next = ListNode(val % 10)
                temp = temp.next
                l1, l2 = l1.next, l2.next
                
            # Update carry
            carry = 1 if val >= 10 else 0
            
        if carry == 1:
            temp.next = ListNode(1)
            
        return s.next
    
    # Time: O(n)
    # Space: 0(1)