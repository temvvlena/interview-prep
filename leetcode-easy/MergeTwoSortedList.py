# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2) :
        # Dummy-ыг заавал хадгалж байж тухайн холбогдсон листийг алдахгүй барих болно
        # cur гэдэг нь Dummy Толгойг түүний сүүлтэй холбож өгөхөд ашиглана
        
        dummy = cur = ListNode(0)
        while l1 and l2:
            # val1-ийг val2 тай харьцуулж байж, хамгийн бага утгыг Dummy-ын cur тэй холбож өгнө
            # Дараа нь l1 эсвэл l2 оо нэг листээр дээшлүүлж өгөх хэрэгтэй
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            # cur-ийг шинэ cur-лүү холбож өгнө
            cur = cur.next
        # Хамгийн сүүлд үлдсэн болгоныг лист ийн хамгийн сүүлийн утган дээр шууд нэмэх нь       
        cur.next = l1 or l2
        return dummy.next
l1 = ListNode(1)
b = ListNode(2)
c = ListNode(4)
l1.next = b
b.next = c
l2 = ListNode(1)
bb = ListNode(3)
cc = ListNode(5)
l2.next = bb
bb.next = cc

calling = Solution()
calling.mergeTwoLists(l1, l2)

