# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        Node = ListNode(None)
        curNode = Node
        while(l1 != None or l2 != None):
            if (l2 == None or l1 != None and l1.val <= l2.val):
                curNode.next = l1
                l1 = l1.next
            else:
                curNode.next = l2
                l2 = l2.next
            curNode = curNode.next
        return Node.next
