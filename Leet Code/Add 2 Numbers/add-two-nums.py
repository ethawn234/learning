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

# ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
# ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 4, next: None}}}

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        l3 = head
        carry = 0

        while l1 is not None or l2 is not None:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            carry = total // 10

            l3.next = ListNode(total % 10)
            l3 = l3.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
            if carry > 0:
                l3.next = ListNode(carry)
        return head.next




































    @staticmethod
    def addTwoNumbers4(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        carry = 0
        nextNode = l3
        
        # issue is I built the condition `while l1.next is not None`
        # condition statement is valid but incorrect for use case - terminates at less iterations than required
        # l1.next makes one less traversal because it is in effect checking for the presence of the next node, not
        # the current node as in `while l1 is not None`. Using the the node as a whole, as in the just-mentioned
        # condition statement, `while l1 is not None` gives me the desired number of loops because there will be
        # by definition of the Node Class a value associated.
        # the valid condition `l1 is not None` makes the exact required iterations to get every node
            # l1 is not None -> checks the current node in the loop
            # l1.next is not None -> checks the current nodes NEXT node
        while l1 is not None:
            total = l1.val + l2.val + carry
            carry = total // 10
            val = total % 10

            nextNode.next = ListNode(val)
            nextNode = nextNode.next

            l1 = l1.next
            l2 = l2.next

        # Check if there is any remaining carry
        if carry > 0:
            nextNode.next = ListNode(carry)
        print('The result is:\n' + '\t\t' +  l3.next.to_string())

    # same call and args returns ListNode{val: 7, next: ListNode{val: 0, next: ListNode{val: 1, next: None}}}





























    @staticmethod
    def addTwoNumbers3(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create the head node
        l3 = ListNode(l1.val + l2.val)
        # create the placeholder for traversal which gets continually reassigned
        current_node = ListNode()
        l3.next = current_node
        carried_remainder = 0

        # assuming both linked lists are equal length
        # while there is another node
        # calculate `val`
        # calculate `next`
        # reassign loop control variable
        # reassign traversal placeholder with current valid values

        # account for sums > 9; `//` operator -> floor division

    # ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
    # ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 4, next: None}}}
        # print('l1: ' + l1.to_string(), '\n l2: ', l2.to_string())
        i = 0
        while l1.next is not None:
            # print(current_node.to_string())
            current_sum = l1.val + l2.val
            total_sum = current_sum + carried_remainder
            sum = 0
            if carried_remainder > 9:
                sum = 9
                total_sum -= sum

            current_node.val = total_sum
            current_node.next = ListNode()
            l1 = l1.next
            l2 = l2.next
            carried_remainder = total_sum
            print(i, total_sum)
            i+=1
            











    @staticmethod
    def addTwoNumbers2(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l3 = ListNode()
        # l3.head = l1.head.val + l2.head.val? 
        current_node = l3
        
        while l1.next:
            # l1.next = ListNode{val: 4, next: ListNode{val: 3, next: None}} # -> [2,4,3]
            # l2.next = ListNode{val: 6, next: ListNode{val: 4, next: None}} # -> [5,6,4]
            l3 = ListNode()
            l3.val = l1.val + l2.val
            l3.next = ListNode()

        return l3 # [4,3]
    
    @staticmethod
    def addTwoNumbers(l1, l2):
        l0 = []
        l1 = ''.join(map(str, l1))
        l2 = ''.join(map(str, l2))
        l3 = str(int(l1) + int(l2))

        for n in l3:
            l0.append(int(n))


        print(l0)
        
Solution.addTwoNumbers4(ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3))), ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4))))
