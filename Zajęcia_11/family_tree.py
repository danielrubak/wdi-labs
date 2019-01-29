class Person:
    def __init__(self, name, parent=None, spouse=None):
        self.parent = parent
        self.name = name
        self.spouse = spouse
        self.children = []

    def __str__(self):
        per_details = "Name: " + str(self.name)
        if self.parent != "Main root" and self.parent:
            per_details += "    Parents: " + str(self.parent[0].name) + " and " + str(self.parent[1].name)
        if self.spouse:
            per_details += "    Spouse: " + str(self.spouse.name)
        if self.children:
            per_details += "    Childrens: "
            for ch in self.children:
                per_details += str(ch.name) + " "
        return per_details

    def findPerson(self, x):
        if self.name is x: return self
        for node in self.children:
            if node.spouse:
                if node.spouse.name == x: return node.spouse
            n = node.findPerson(x)
            if n: return n
        return None

    def printElements(self, x, spaces):
        for ch in x.children:
            if ch.spouse:
                print("   "*spaces,ch.name,' and ',ch.spouse.name,sep='')
            else:
                print("   "*spaces, ch.name,sep='')
            ch.printElements(ch, spaces+1)

class FamilyTree:
    def __init__(self):
        self.members = 0
        self.root = Person('Main root', None)

    def findMember(self, name):
        n = self.root
        return n.findPerson(name)

    def addMember(self, name, parent):
        if parent == "Main root":
            new_member = Person(name, parent)
            self.root.children.append(new_member)
            self.members += 1
        else:
            isExists = self.findMember(parent)
            parents = []
            if isExists:
                parents.append(isExists)
                if isExists.spouse:
                    parents.append(isExists.spouse)
                new_member = Person(name, parents)
                isExists.children.append(new_member)
                isExists.spouse.children.append(new_member)
                self.members += 1

    def addSpouse(self, name, spouse):
        isExists = self.findMember(spouse)
        if isExists:
            new_member = Person(name, None, isExists)
            isExists.spouse = new_member
            if isExists.children:
                new_member.children = isExists.children
            self.members += 1
        else:
            print("There is no person named",spouse)

    def removeMember(self, name):
        isExists = self.findMember(spouse)
        if isExists:
            if isExists.children:
                print("This person has children")
            else:
                del isExists
                self.members -= 1

    def printTree(self):
        n = self.root
        n.printElements(n, 0)

family_tree = FamilyTree()
family_tree.addMember("Daniel","Main root")
family_tree.addMember("Adam", "Main root")
family_tree.addSpouse("Paulina", "Adam")
family_tree.addMember("Maja", "Adam")
family_tree.addMember("Michał", "Main root")
family_tree.addSpouse("Marta", "Michał")
family_tree.addMember("Zuzia", "Michał")
#print(family_tree.findMember("Zuzia"))
#print(family_tree.findMember("Maja"))
#print(family_tree.findMember("Adam"))
#print(family_tree.findMember("Paulina"))
#print(family_tree.findMember("Michał"))
#print(family_tree.findMember("Marta"))
family_tree.addSpouse("Darek", "Zuzia")
family_tree.addMember("Kamila", "Zuzia")
family_tree.addMember("Monika", "Michał")
family_tree.printTree()
