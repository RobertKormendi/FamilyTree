
class Person():
    def __init__(self, name, parent):
        self.name = name
        self.gen = 0
        self.children = []
        self.parent = parent
    
    def add_child(self, child):
        self.children.append(child)



family = [
Person('Elizabeth', None),
Person('Marj','Elizabeth'),
Person('Rozanne','Elizabeth'),
Person('Ruthanne','Elizabeth'),
Person('Donnie','Elizabeth'),
Person('Patricia','Elizabeth'),
Person('Kim','Marj'),
Person('Monica','Marj'),
Person('Martin','Marj'),
Person('Gabe','Marj'),
Person('John','Marj'),
Person('Ben','Marj'),
Person('Jerome','Marj'),
Person('John G', 'Kim'),
Person('Jamie', 'Kim'),
Person('Julia', 'Kim'),
Person('Phil', 'Monica'),
Person('Alley', 'Monica'),
Person('Anna', 'Monica'),
Person('Steven', 'Monica'),
Person('Lincoln', 'Phil'),
Person('Ellane', 'Gabe'),
Person('Mo', 'Ellane'),
Person('Jake', 'Gabe'),
Person('Jeera', 'Jerome'),
Person('Precila', 'Jerome'),
Person('Clarence', 'Jerome')
]





for each in family:
    for person in family:
        if each.name == person.parent:
            each.add_child(person.name)
            person.gen = each.gen + 1


def findGeneration(x):
    gen = 1
    name = family[x].name
    while family[x].parent != None:
        for i in range(len(family)):
            if family[i].name == family[x].parent:
                x = i
                break
        name = family[x].name
        gen += 1
    return gen

for x in range(len(family)):
    family[x].gen = findGeneration(x)


input = input("Enter a name: ").split()
for x in range(len(input)):
    for i in range(len(family)):
        if family[i].name == input[x]:
            input[x] = i
            break
        elif i == len(family) - 1:
            print(f"Name {input[x]} not found")
            input.pop(x)


for x in range(len(input)):
    print(family[input[0]].gen)
    print(input[x])


def checkRelationship(x, y):
    if family[x].name == family[y].name:
        print(f"{family[x].name} is the same person as {family[y].name}")
    
        
