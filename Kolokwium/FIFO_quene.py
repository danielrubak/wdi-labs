class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
    def __del__(self):
        return "Element " + str(self.name) + " has been removed!"
    def __str__(self):
        return "Name: " + str(self.name)

class Quene:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, name):
        new_node = Node(name);
        if not self.head:
            self.head =  new_node
        else:
            temp = self.head
            self.head = new_node
            new_node.next = temp
        self.size += 1

    def pop(self):
        if not self.head:
            print("There is no element to pop!")
        elif self.size != 0:
            temp = self.head
            self.head = temp.next
            del temp
        elif self.size == 0:
            del self.head
        self.size -= 1

    def printQuene(self):
        if self.size == 0:
            print("Quene is empty!")
        else:
            n = self.head
            while(n):
                print(n)
                n = n.next

newQuene = Quene()
newQuene.push("First element")
newQuene.push("Second element")
newQuene.push("Third element")
newQuene.printQuene()
print()
newQuene.pop()
newQuene.printQuene()
print()
newQuene.pop()
newQuene.printQuene()
