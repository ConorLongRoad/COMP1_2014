import random

class Crop:
    """A generic food crop"""

    #Constructor (run automatically when you use the class)

    def __init__(self, growthRate, lightNeed, waterNeed):
        #Set the attributes with an initial value
        #It's similar to stats in Fifa, e.g. speed: 67, stamina: 44

        self._growth = 0
        self._daysGrowing = 0
        self._growthRate = growthRate
        self._lightNeed = lightNeed
        self._waterNeed = waterNeed
        self._status = "Seed"
        self._type = "Generic"

        #The above attributes are prefixed with an underscore to indicate that
        #they should not be accessed or altered directly from outwith the class

    #These are methods. These are easy to reach and are in direct contact with the class

    def needs(self):
        #Returns a dictionary containing the light and water needs
        #A dictionary is like a list, except instead of accessing values in the list using values, you use keys

        return {"Light need": self._lightNeed, "Water need": self._waterNeed}

    def report(self):
        #Return a dictionary containing the type, status, growth and days growing

        return {"Type": self._type, "Status": self._status, "Growth": self._growth, "Days growing": self._daysGrowing}

    def updateStatus(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"

    def grow(self, light, water):
        if light >= self._lightNeed and water >= self._waterNeed:
            self._growth += self._growthRate

        #Add 1 to number of days growing
        self._daysGrowing += 1

        #Update the status of the crop
        self.updateStatus()

def autoGrow(crop, days):
    #Grow the crop

    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manualGrow(crop):
    #Get the light and water values from the user

    #Check the light value is correct
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light values (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Value entered not valid. Please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid. Please enter a value between 1 and 10")

    #Check the water value is correct
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid. Please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid. Please enter a value between 1 and 10")

    #Grow the crop
    crop.grow(light,water)

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

def manageCrop(crop):
    
    print("This is the crop management program")
    print()
    
    noExit = True
    while noExit:
        displayMenu()
        option = getMenuChoice()
        print()
        
        if option == 1:
            manualGrow(crop)
        elif option == 2:
            autoGrow(crop,30)
        elif option == 3:
            print(crop.report())
        elif option == 0:
            noExit = False
            print()
    print("Thank you for using the crop management program")

def main():
    
    #Instantiate the class by giving it preset values
    newCrop = Crop(1,4,3)

    #Task 1
    #Test to see whether it works or not
    #print(newCrop._status)
    #print(newCrop._lightNeed)
    #print(newCrop._waterNeed)

    #Task 2
    #Be able to make different classes from the same variables
    #newCrop2 = Crop(2,5,7)
    #print(newCrop._status)
    #print(newCrop._lightNeed)
    #print(newCrop._waterNeed)

    #Task 3
    #print(newCrop.needs()["Light need"])
    #print(newCrop.report())

    #Task 5a
    #autoGrow(newCrop,30)

    #Task 5b
    #manualGrow(newCrop)

    #Task 4
    #newCrop.grow(4,4)
    #print(newCrop.report())

    #Task 6
    manageCrop(newCrop)
    

if __name__ == "__main__":
    main()
