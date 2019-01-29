class Node:
    def __init__ (self, name, priority):
        self.name = name;
        self.priority = priority;
        self.next = None;
        self.prev = None;

    def __str__(self):
        return "Task: " + str(self.name) + ", Priority: " + str(self.priority)

    def __del__ (self):
        return "Task: " + str(self.name) + " has been removed!"

class Organizer:
    def __init__ (self):
        self.head = None;
        self.tail = None;
        self.size = 0;

    def add(self, name, priority):
        new_node = Node(name, priority)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            if self.head.priority < new_node.priority:
                temp = self.head
                temp.prev = new_node
                new_node.next = temp
                self.head = new_node
            elif self.tail.priority > new_node.priority:
                temp = self.tail
                temp.next = new_node
                new_node.prev = temp
                self.tail = new_node
            else:
                temp = self.head
                while(temp.priority>=new_node.priority):
                    temp = temp.next
                temp2 = temp.prev
                temp2.next = new_node
                new_node.next = temp2
                temp.prev = new_node
                new_node.next = temp

        self.size += 1

    def printOrganizer(self):
        if self.size == 0:
            print('List is empty!')
        else:
            n = self.head
            while(n):
                print(n)
                n = n.next

newOrganizer = Organizer()
newOrganizer.add("Zadanie 1", 2)
newOrganizer.add("Zadanie 2", 5)
newOrganizer.add("Zadanie 3", 1)
newOrganizer.add("Zadanie 4", 3)
newOrganizer.printOrganizer()
