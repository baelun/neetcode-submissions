# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return


        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next #把slow後面的建立一個新的linkedlist
        slow.next = None  #把原本linkedlist後的切斷


        prev = None
        current = second
        while current:    
            nxt=current.next
            current.next = prev
            prev = current
            current = nxt
        
        first,second_head = head,prev

        while second_head:
            tmp_1 = first.next
            tmp_2 = second_head.next

            first.next = second_head
            second_head.next = tmp_1

            first = tmp_1
            second_head = tmp_2
           

