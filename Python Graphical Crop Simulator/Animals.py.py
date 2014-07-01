from Cow_Class import *
from Sheep_Class import *

def displayMenu():
    
    print()
    print("Which animal would you like to create?")
    print()
    print("1. Cow")
    print("2. Sheep")
    print()
    print("Please select an option from the above menu")

def selectOption():
    
    validOption = False
    
    while not validOption:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,2):
                validOption = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
            
    return choice

def createAnimal():
    
    displayMenu()
    choice = selectOption()

    if choice == 1:
        newAnimal = Cow()
    elif choice == 2:
        newAnimal = Sheep()

    return newAnimal

def main():
    newAnimal = createAnimal()
    manageAnimal(newAnimal)

if __name__ == "__main__":
    main()

