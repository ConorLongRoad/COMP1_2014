from Wheat_Class import *
from Potato_Class import *

def displayMenu():
    
    print()
    print("Which crop would you like to create?")
    print()
    print("1. Potato")
    print("2. Wheat")
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

def createCrop():
    
    displayMenu()
    choice = selectOption()

    if choice == 1:
        newCrop = Potato()
    elif choice == 2:
        newCrop = Wheat()

    return newCrop

def main():
    newCrop = createCrop()
    manageCrop(newCrop)

if __name__ == "__main__":
    main()
