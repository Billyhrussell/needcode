# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, Sequence

class Solution(object):
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev, curr = None, head
        # prev = None, curr = head

        while curr:
            # while still in list
            print("CURR ", curr.val)
            
            temp = curr.next
            print("temp = CURR.next ,", temp)

            curr.next = prev
            print("curr.next = prev ,", prev)

            prev = curr
            print("prev = curr ,", prev.val)

            curr = temp
            print("curr = temp ,", curr)
        return prev

a = [1,2,3,4,5]
head = ListNode(a)
print("HEAD.VAL = ", head.val)
solution = Solution()
print(solution.reverseList(head))