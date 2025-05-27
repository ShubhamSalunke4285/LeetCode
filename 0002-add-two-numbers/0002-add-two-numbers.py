# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        # Head of the new linked list - this is the head of the resultant list
        head = None
        # Reference of head which is null at this point
        temp = None
        # Carry
        carry = 0
        # Loop for the two lists
        while l1 is not None or l2 is not None:
            # At the start of each iteration, we should add carry from the last iteration
            sum_value = carry
            # Since the lengths of the lists may be unequal, we are checking if the
            # current node is null for one of the lists
            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next
            # At this point, we will add the total sum_value % 10 to the new node
            # in the resultant list
            node = ListNode(sum_value % 10)
            # Carry to be added in the next iteration
            carry = sum_value // 10
            # If this is the first node or head
            if temp is None:
                temp = head = node
            # for any other node
            else:
                temp.next = node
                temp = temp.next
        # After the last iteration, we will check if there is carry left
        # If it's left then we will create a new node and add it
        if carry > 0:
            temp.next = ListNode(carry)
        return head

        # a = 0
        # for i in l1:
        #     a = a*10 + i
        # a1=str(a)

        # b = 0
        # for i in l2:
        #     b = b*10 + i
        # b1= str(b)

        # c = str(int(a1[::-1]) + int(b1[::-1]))
        # f=[]
        # for i in c[::-1]:
        #     f.append(i)
        # print(f)
