
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
      
        def merge_two_sorted_lists(l1, l2):
            dummy = ListNode(0)
            current = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            
            if l1:
                current.next = l1
            else:
                current.next = l2
            return dummy.next

       
        if not lists:
            return None

      
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged_lists.append(merge_two_sorted_lists(lists[i], lists[i + 1]))
                else:
                    merged_lists.append(lists[i])
            lists = merged_lists

        return lists[0]

