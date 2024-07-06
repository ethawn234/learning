from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_string(self):
        """Stringify the result"""
        if self.next:
            return f"ListNode{{val: {self.val}, next: {self.next.to_string()}}}"
        else:
            return f"ListNode{{val: {self.val}, next: None}}"

class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()  # Dummy node to simplify handling the head of the result list
        nextNode = l3
        carry = 0
        
        while l1 is not None or l2 is not None:
            val1 = l1.val
            val2 = l2.val
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            nextNode.next = ListNode(total % 10)
            
            # Move to the next nodes in the lists
            nextNode = nextNode.next
            l1 = l1.next
            l2 = l2.next
        
        # Check if there is any remaining carry
        if carry > 0:
            nextNode.next = ListNode(carry)
        
        print(l3.next.to_string())
    
       
Solution.addTwoNumbers(ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3))), ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4))))
# returns ListNode{val: 7, next: ListNode{val: 0, next: ListNode{val: 8, next: None}}}
