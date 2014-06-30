import random

class Animal:
    """A generic animal"""

    def __init__(self, growthRate, foodNeed, waterNeed):
        #Set attributes with initial values

        self._weight = 0
        self._daysGrowing = 0
        self._growthRate = growthRate
        self._foodNeed = foodNeed
        self._waterNeed = waterNeed
        self._status = "Baby"
        self._type = "Generic"
        self._name = "Sean"

    def needs(self):

        return {"Food need": self._foodNeed, "Water need": self._waterNeed}

    def report(self):

        return {"Type": self._type, "Name": self._name, "Status": self._status, "Weight": self._weight, "Days growing": self._daysGrowing}

    def updateStatus(self):
        if self._weight > 15:
            self._status = "Old"
        elif self._weight > 10:
            self._status = "Mature"
        elif self._weight > 5:
            self._status = "Young"
        elif self._weight > 0:
            self._status = "Toddler"
        elif self._weight == 0:
            self._status = "Baby"

    def grow(self, food, water):
        if food >= self._foodNeed and water >= self._waterNeed:
            self._weight += self._growthRate

        #Add 1 to number of days growing
        self._daysGrowing += 1

        #Update the status of the animal
        self.updateStatus()

def autoGrow(animal,days):
    #Grow the animal

    for day in range(days):
        food = random.randint(1,100)
        water = random.randint(1,10)
        animal.grow(food,water)
        
def manualGrow(animal):
    #Get the food and water values from the user

    #Check the food value is correct

    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-100): "))
            if 1 <= food <= 100:
                valid = True
            else:
                print("Value entered not valid. Please enter a value between 1 and 100")
        except ValueError:
            print("Value entered not valid. Please enter a value between 1 and 100")

    #Check the water value is correct

    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid. Please enter a value between 1 and 100")
        except ValueError:
            print("Value entered not valid. Please enter a value between 1 and 100")

    #Grow the animal
    animal.grow(food,water)

def displayMenu():

    print()
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print()
    print("Please select an option from the above menu")

def getMenuChoice():

    optionValid = False

    while not optionValid:
        try:
            choice = int(input("Option selected: "))
            if 0 <= choice <= 4:
                optionValid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")

    return choice

def manageAnimal(animal):

    print("This is the crop management program")
    print()

    noExit = True

    while noExit:
        displayMenu()
        option = getMenuChoice()
        print()

        if option == 1:
            manualGrow(animal)
        elif option == 2:
            autoGrow(animal,30)
        elif option == 3:
            print(animal.report())
        elif option == 0:
            noExit = False
            print()

    print("Thank you for using the crop management program")

def main():

    newAnimal = Animal(1,40,3)

    manageAnimal(newAnimal)

if __name__ == "__main__":
    main()
