class LinkedList:
    class Node:
        def __init__(self, val = 0,  next = None):
            self.val = val
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    
    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
    
        idx = 0
        curr = self.head

        while idx < index and curr.next:
            curr = curr.next
            idx += 1

        return curr.val
        

    def insertHead(self, val: int) -> None:
        new_node = self.Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        print(self.getValues())
        

        

    def insertTail(self, val: int) -> None:
        new_node = self.Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        print(self.getValues())
        
        

    def remove(self, index: int) -> bool:
        if index >= self.size or index < 0:
            return False
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        
        idx = 0
        curr = self.head

        while idx < index - 1:
            curr = curr.next
            idx += 1
        
        if index == self.size - 1:
            self.tail = curr 
        curr.next = curr.next.next
        self.size -= 1
        print(self.getValues())
        return True

        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head

        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
