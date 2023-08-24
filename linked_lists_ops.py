class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLinkedList:
    def create(self, node, data):
        node.next = Node(data)
        return node
    
    def display(self, node: Node):
        temp = node
        toDisplay = ''
        while(temp != None ):
            toDisplay += temp.data + '->'
            temp = temp.next
        return toDisplay

    def reverse(self, node: Node):
        current = node
        prev = None
        next = None
        while(current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        
        return prev
    
if __name__ == "__main__":

   a = Node('a')
   b = Node('b')
   c = Node('c')
   d = Node('d')

   a.next = b
   b.next = c
   c.next = d

   linked_list = CLinkedList()
#    print(linked_list.display(a))
   reversed = linked_list.reverse(a)
   print(linked_list.display(reversed))


   
    
