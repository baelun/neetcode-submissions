# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        slow = fast = dummy
        
        for _ in range(n+1):  #先讓 fast 走 n 步(加上dummy本身是n+1步)，到時候兩個距離就是n
            fast = fast.next

        while fast:
            # 讓fast走到底
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next