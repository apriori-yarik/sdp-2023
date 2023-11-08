class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value, position):
        new_Node = Node(value)
        self.size += 1
        if self.head is None:
            self.head = new_Node
            return
        
        if position == 0:
            new_Node.next = self.head
            self.head = new_Node
        elif position == self.size:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_Node
        elif position > 0 and position < self.size:
            current_node = self.head
            counter = 0
            while counter + 1 != position:
                current_node = current_node.next
                counter += 1

            new_Node.next = current_node.next
            current_node.next = new_Node
        else:
            print("Index out of range")

    def removeByIndex(self, position):
        if self.head is None:
            print("Empty linked list")
            return
        
        if position == 0:
            current_node = self.head
            self.head = current_node.next
        elif position == self.size - 1:
            current_node = self.head
            if current_node.next is None:
                self.head = None
                return
            while current_node.next.next != None:
                current_node = current_node.next
            current_node.next = None
        elif position > 0 and position < self.size - 1:
            current_node = self.head
            counter = 0
            while counter+1 != position:
                current_node = current_node.next
                counter += 1
            current_node.next = current_node.next.next

        self.size -= 1

    def removeByValue(self, value):
        if self.head is None:
            print("No elements in linked list")
            return
        
        current_node = self.head
        if current_node.data == value:
            self.head = current_node.next
        while current_node.next.data != value:
            current_node = current_node.next

        if current_node.next.next is None:
            current_node.next = None
        else:
            current_node.next = current_node.next.next

        self.size -= 1

    def update(self, position, value):
        if self.head is None:
            print("Empty list")
            return
        
        current_node = self.head
        counter = 0

        if position >= self.size:
            print("Index out of range")
            return

        while counter != position:
            current_node = current_node.next
            counter += 1
        current_node.data = value

    def print(self):
        if self.head is None:
            print("Empty")
            return

        current_node = self.head
        ll = []
        while current_node != None:
            ll.append(current_node.data)
            current_node = current_node.next
        print(" ".join([str(x) for x in ll]))


ll = LinkedList()

ll.add(5, 0)
ll.add(4, 0)
ll.add(3, 0)

ll.print()

ll.update(0, 4)
ll.update(1, 10)
ll.update(2, 45)

ll.print()

ll.removeByValue(10)
ll.removeByValue(45)

ll.print()

ll.add(20, 1)
ll.add(30, 2)
ll.add(10, 3)

ll.print()

ll.removeByIndex(2)
ll.removeByIndex(0)
ll.removeByIndex(1)

ll.print()
