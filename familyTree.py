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




for person in family:
    for parent in family:
        if person.parent is None:
            break;
        elif parent.name == person.parent:
            person.parent = parent
            break;



# for each in family:
#     for person in family:
#         if each.name == person.parent:
#             each.add_child(person.name)
#             person.gen = each.gen + 1


def findGeneration(x):
    gen = 1
    person = family[x]
    while person.parent != None:
        person = person.parent
        gen += 1
    return gen
    

for x in range(len(family)):
    family[x].gen = findGeneration(x)

# find index of each input
input = input("Enter a name: ").split()
for x in range(len(input)):
    for i in range(len(family)):
        if family[i].name == input[x]:
            input[x] = i
            break
        elif i == len(family) - 1:
            print(f"Name {input[x]} not found")
            input.pop(x)


# for x in range(len(input)):
#     print(f"{family[input[x]].name}")
#     print(f"{family[input[x]].gen}")


def higherOrLower(i1, i2):
    p1 = family[i1]
    p2 = family[i2]
    
    if p1.gen > p2.gen:
        higher = p1
        lower = p2
    else:
        higher = p2
        lower = p1        
        
    return([higher, lower])
    
    # for x in range(higher.gen - lower.gen):
    #     check = check.parent
        
    # return(check.name)


myList = higherOrLower(input[0], input[1])

def findAncestor(higher, lower):
    check = higher
    
    for x in range(higher.gen - lower.gen):
        check = check.parent #find the person in higher's lineage that is in lower's generation. If that is the same person as lower, then its solved
        
    if check == lower:
        return(1)
        
    else:
        check2 = lower
        for x in range(lower.gen):
            check2 = check2.parent
            check = check.parent
            if check == check2:
                break; #check is now the common ancestor
                
    difference1 = higher.gen - check.gen
    difference2 = lower.gen - check.gen
    return([difference1, difference2])
            
genDifferences = findAncestor(myList[0], myList[1])

def getSuffix(n):
    
    if 10 <= n % 100 <= 20:
        suffix = 'th'
        
    else: suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, 'th')
    return(suffix)
    
def getRelation(differences):
    if differences == 1:
        genDiff = myList[0].gen - myList[1].gen
        if genDiff == 1:
            return 'child'
        elif genDiff == 2:
            return 'grandchild'
        elif genDiff > 2:
            return "great " * (genDiff - 2) + "grandchild"

print(getRelation(genDifferences))
    


    
    
    

# def checkRelationship(x, y):
#     if family[x].name == family[y].name:
#         print(f"{family[x].name} is the same person as {family[y].name}")
    
        
