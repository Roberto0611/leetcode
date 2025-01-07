'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
 Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

leetcode problem link:https://leetcode.com/problems/add-two-numbers/description/ 
'''
# Important to remember: For this problem leetcode use listNodes not lists.

# stablish ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # value to assign the value
        self.next = next  # next node

# solution start:
def addTwoNumbers(l1,l2):
        # We are going to create a function to join the numbers of the array
        def joinNumbers(list):

            x = ''
            current = list
            while current: # Until last 
                x+=str(current.val)
                current = current.next
            return(x[::-1])            
            
        number1 = joinNumbers(l1)
        number2 = joinNumbers(l2)

        result = str(int(number1) + int(number2))[::-1]  # Result inverted

        # Create the node to output
        dummy = ListNode()
        current = dummy

        for digit in result:
            current.next = ListNode(int(digit))
            current = current.next
        
        return dummy.next


# Test the function

# assign the values
l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))

# Print the function
print(addTwoNumbers(l1,l2))

# -------- ListNode tests--------


'''
# Iterate over the ListNode
current = l1
while current:
    print(current.val, end=" -> ")
    current = current.next
'''   