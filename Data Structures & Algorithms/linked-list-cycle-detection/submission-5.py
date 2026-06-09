# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        path = set()
        if head != None:
            head_val = head.val
        while head:
            next = head.next
            if not next:
                return False
            if next.val in path:
                return True
            else:
                path.add(next.val)
                head = next.next
        return False
