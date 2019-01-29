class Node:

    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.next = None
        self.prev = None

    def __str__(self):
        return 'Student name: ' + str(self.name) + '    Points: ' + str(self.points)

    def __del__(self):
        return 'Student ' + str(self.name) + ' has been removed'

class BidirectionalList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_tail(self, name, points):
        if not self.head:
            n = Node(name, points)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            n = self.tail
            new_node = Node(name, points)
            n.next = new_node
            new_node.prev = n
            new_node.next = None
            self.size += 1
            self.tail = new_node

    def remove_tail(self):
        if not self.head:
            print("List is empty!")
        elif self.size == 1:
            n = self.head
            del n
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            n = self.tail
            prev_node = n.prev
            prev_node.next = None
            self.tail = prev_node
            self.size -= 1
            del n

    def add_head(self, name, points):
        if not self.head:
            n = Node(name, points)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            n = self.head
            new_node = Node(name, points)
            new_node.next = n
            new_node.prev = None
            n.prev = new_node
            self.size += 1
            self.head = new_node

    def remove_head(self):
        if not self.head:
            print("List is empty!")
        elif self.size == 1:
            n = self.head
            del n
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            n = self.head
            next_node = n.next
            next_node.prev = None
            self.head = next_node
            self.size -= 1
            del n

    def add_on_position(self, name, points, pos):
        if pos == 1:
            self.add_head(name, points)
        elif pos == self.size+1:
            self.add_tail(name, points)
        elif pos>1 and pos<(self.size+1):
            if pos > (self.size/2):
                n = self.tail
                while (self.size - pos):
                    n = n.prev
                    pos -= 1
            else:
                n = self.head
                while (pos-1):
                    n = n.next
                    pos -= 1

            prev_node = n.prev
            new_node = Node(name, points)
            prev_node.next = new_node
            new_node.prev = prev_node
            n.prev = new_node
            new_node.next = n
            self.size += 1
        else:
            print("Wrong position!")

    def printListFromHead(self):
        if self.size == 0:
            print('List is empty!')
        else:
            n = self.head
            while n:
                print(n)
                n = n.next

    def printListFromTail(self):
        if self.size == 0:
            print('List is empty')
        else:
            n = self.tail
            while n:
                print(n)
                n = n.prev

    def printDetails(self):
        print("List size:",self.size)
        print("List head:",self.head)
        print("List tail:",self.tail)

    def findBestScore(self):
        maxScore = -1
        bestNode = None
        n = self.head
        while n:
            if n.points > maxScore:
                maxScore = n.points
                bestNode = n
            n = n.next
        print("Best result:")
        print(bestNode)

newList = BidirectionalList()
newList.add_tail("Rubak", 14)
newList.add_head("Krzysiek", 12)
newList.add_on_position("Kwiatek", 13, 2)

print("List printed from begin:")
newList.printListFromHead()
print("\nList printed from end:")
newList.printListFromTail()
print()
newList.findBestScore()
newList.remove_head()
print("\nList after object removed:")
newList.printListFromHead()
newList.remove_tail()
print("\nList after object removed:")
newList.printListFromHead()
#newList.printDetails()
