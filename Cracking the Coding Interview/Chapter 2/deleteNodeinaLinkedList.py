#Delete Node in a Linked List
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
