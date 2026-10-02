# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dumbyNode = ListNode()
        cur = dumbyNode
        cur1, cur2 = list1, list2
        while cur1 or cur2:
            if cur1 is None:
                cur.next = cur2
                cur2 = cur2.next
            elif cur2 is None:
                cur.next = cur1
                cur1 = cur1.next
            elif cur1.val >= cur2.val:
                cur.next = cur2
                cur2 = cur2.next
            else:
                cur.next = cur1
                cur1 = cur1.next
            cur = cur.next
        return dumbyNode.next
            
