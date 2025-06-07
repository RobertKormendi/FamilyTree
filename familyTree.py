class Person():
    def __init__(self, name, parent):
        self.name = name
        self.gen = 0
        self.children = []
        self.parent = parent
    



family = [
Person("Adam", None),
Person("Beth", "Adam"),
Person("Carl", "Adam"),
Person("Dana", "Carl"),
Person("Eve", "Carl"),
Person("Frank", "Dana"),
Person("Grace", "Eve"),
Person("Hank", "Dana"),
Person("Ivy", "Eve"),
Person("Jack", "Grace"),
Person("Kara", "Grace"),
Person("Liam", "Ivy"),
Person("Mona", "Liam"),
Person("Nate", "Jack"),
Person("Olive", "Kara"),
Person("Pete", "Olive"),
Person("Quinn", "Mona"),
Person("Rita", "Liam"),
Person("Sam", "Quinn"),
Person("Tina", "Jack")
]



#assign each person their parent's object rather than just a string
for person in family: 
    for parent in family:
        if person.parent is None:
            break;
        elif parent.name == person.parent:
            person.parent = parent
            break;





def findGeneration(x): #assign each member their generation number
    gen = 1
    person = family[x]
    while person.parent != None:
        person = person.parent
        gen += 1
    return gen
    

for x in range(len(family)):
    family[x].gen = findGeneration(x)


def getInput():

    while True:
        error  = False
        myInput = input("Enter two comma separated names: ").replace(" ", "").split(',') # map input to a list
        if len(myInput) == 2: #make sure that 2 names were given
            for x in range(len(myInput)):
                for i in range(len(family)):
                    if family[i].name == myInput[x]:
                        myInput[x] = family[i]
                        break
                    elif i == len(family) - 1:
                        print(f"Error! Name {myInput[x]} not found")
                        error = True 
                        break;
        else:
            print("make sure they're comma separated")
            error = True
        if error == False: #only exit the loop if a valid input is given
            break;
    return(myInput[0], myInput[1])




def higherOrLower(p1, p2): #find which person has the higher generation number
    
    if p1.gen > p2.gen:
        higher = p1
        lower = p2
        
    else:
        higher = p2
        lower = p1
        
    return(higher, lower)



def findAncestor(higher, lower): 
    if higher == lower: # check if they are the same person
        return(0) # 0 is an arbitrary value that I use to check in the end
    check = higher
    
    for x in range(higher.gen - lower.gen):
        check = check.parent #find the person in higher's lineage that is in lower's generation.
        
    if check == lower: #check if the person in higher's lineage at lower's generation is lower
        return(1) #also arbitrary
        
    else:
        check2 = lower 
        while check.parent is not None: #make sure that the loop ends at ancestor
            check2 = check2.parent #iterate over the lineages of both people
            check = check.parent   #until a common ancestor is found
            if check == check2:
                break; #check is now the common ancestor
                
    difference1 =  person1.gen - check.gen 
    difference2 = person2.gen - check.gen
    return([difference1, difference2]) #returns the difference in generation between each person and the common ancestor
            

def getSuffix(n):
    
    if 10 <= n % 100 <= 20: #special cases between 10 and 20
        suffix = 'th'
        
    else: suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, 'th')
    return(suffix) #otherwise check if they end with 1, 2 or 3
    
def numToTimes(n):
    suffixes = {1: "once", 2: "twice", 3: "thrice"}
    return suffixes.get(n, f"{n} times") 
    
    
def getRelation(differences):
    if differences == 0: #arbitrary number is used here
        return(f"{person1.name} and {person2.name} are the same person")
        
# if they are of the same lineage, use the difference in their generation numbers to assign the correct message
    elif differences == 1: 
        genDiff = person1.gen - person2.gen
        if genDiff == 1:
            return(f" {person1.name} is the child of {person2.name}")
        elif genDiff == 2:
            return (f" {person1.name} is the grandchild of {person2.name}")
        elif genDiff > 2:
            return(f"{person1.name} is the {"great " * (genDiff - 2)}grandchild of {person2.name}")
        elif genDiff == -1:
            return(f" {person1.name} is the parent of {person2.name}")
        elif genDiff == -2:
            return(f" {person1.name} is the grandparent of {person2.name}")
        elif genDiff < -2:
            return(f"{person1.name} is the {"great " * (genDiff - 2)}grandparent of {person2.name}")            
    else:
        cousin = differences[0] #assign how manyth cousin
        timesRemoved = differences[1] #assign how many times removed they are
        
        #call getSuffix() and numToTimes() to get the correct numbers in the print message
        return(f"{person1.name} and {person2.name} are {cousin}{getSuffix(cousin)} cousins {numToTimes(timesRemoved)} removed ")
   
while True:
    person1, person2 = getInput() #call input function
    myList = higherOrLower(person1, person2)
    genDifferences = findAncestor(myList[0], myList[1])
    #call getRelation() to find the print message
    print(getRelation(genDifferences))
    goAgain = input("Type 'yes' (or anything) to check another pair, or 'no' to exit")
    if goAgain == "no":
        break;
    
    
