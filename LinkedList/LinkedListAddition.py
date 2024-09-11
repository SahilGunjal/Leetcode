"""
Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Solution:
    # Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        def reverse_list(num):
            prev = None
            temp = num
            next_ptr = None

            while temp:
                next_ptr = temp.next
                temp.next = prev
                prev = temp
                temp = next_ptr

            return prev

        def linkedlistaddition(first, second):
            head = None
            ptr = None
            carry = 0
            first_val = 0
            second_val = 0
            while first or second:
                if first is None:
                    first_val = 0
                else:
                    first_val = first.data

                if second is None:
                    second_val = 0

                else:
                    second_val = second.data

                val = first_val + second_val + carry
                if val > 9:
                    carry = int(str(val)[0])
                    temp_val = int(str(val)[1])
                else:
                    carry = 0
                    temp_val = val

                if temp_val == 0 and carry == 0:
                    break

                temp_node = Node(temp_val)

                if head is None:
                    head = temp_node
                    ptr = head

                else:
                    ptr.next = temp_node
                    ptr = ptr.next

                if first:
                    first = first.next
                if second:
                    second = second.next

            if carry != 0:
                ptr.next = Node(carry)

            return reverse_list(head)

        first_num = reverse_list(num1)
        second_num = reverse_list(num2)

        return linkedlistaddition(first_num, second_num)