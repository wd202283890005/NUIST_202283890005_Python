def studList():
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
    
    for name in studentNames:
        print(f"{name} Evans")

    return studentNames

def addToList(studentNames):
    newName = input("Enter a new name to add to the list: ")
    
    studentNames.append(newName)  

    print("\nUpdated list:")
    for name in studentNames:
        print(f"{name} Evans")

studentNames = studList()
    
 
addToList(studentNames)
