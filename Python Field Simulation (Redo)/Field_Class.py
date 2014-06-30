import random

from Potato_Class import *
from Wheat_Class import *
from Cow_Class import *
from Sheep_Class import *

class Field:
    """Simulate a field that can contain animals and crops"""

    #Constructor
    def __init__(self, maxAnimals, maxCrops):
        self._crops = []
        self._animals = []
        self._maxAnimals = maxAnimals
        self._maxCrops = maxCrops

    def plantCrop(self, crop):
        if len(self._crops) < self._maxCrops:
            self._crops.append(crop)
            return True
        else:
            return False

    def addAnimal(self, animal):
        
        if len(self._animals) < self._maxAnimals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvestCrop(self, position):
        return self._crops.pop(position)

    def removeAnimal(self, position):
        return self._animals.pop(position)

    def reportContents(self):
        
        cropReport = []
        animalReport = []
        
        for crop in self._crops:
            cropReport.append(crop.report())
        for animal in self._animals:
            animalReport.append(animal.report())
        return {"Crops": cropReport, "Animals": animalReport}

    def reportNeeds(self):
        
        food = 0
        light = 0
        water = 0
        
        for crop in self._crops:
            needs = crop.needs()
            if needs["Light need"] > light:
                light = needs["Light need"]
            if needs["Water need"] > water:
                water = needs["Water need"]

        for animal in self._animals:
            needs = animal.needs()
            food += needs["Food need"]
            if needs["Water need"] > water:
                water = needs["Water need"]
                
        return {"Food": food, "Light": light, "Water": water}

    def grow(self, light, food, water):
        
        #Grow the crops (light and water are available to all crops in the same amount
        if len(self._crops) > 0:
            
            for crop in self._crops:
                crop.grow(light, water)

        #Grow th animals (water available to all animals in the same amounts
        #But food is a total that must be shared
                
        if len(self._animals) > 0:
            foodRequired = 0
            for animal in self._animals:
                needs = animal.needs()
                foodRequired += needs["Food need"]
                
        #If we have more food available than is required to work out the addition available food
            if food > foodRequired:
                additionalFood = food - foodRequired
                food = foodRequired
            else:
                additionalFood = 0

            for animal in self._animals:
                #Get the animals food needs
                needs = animal.needs()
                
                if food >= needs["Food need"]:
                    #Remove food for this animal from total
                    food -= needs["Food need"]
                    feed = needs["Food need"]
                    #See if there's any additional food to give
                    if additionalFood > 0:
                        #Remove some additional food for this animal
                        additionalFood -= 1
                        #Add this to the feed to be given to the animals
                        feed += 1
                    #Grow the animal
                    animal.grow(feed,water)

def autoGrow(field, days):
    #Grow the field automatically over x days

    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,100)
        field.grow(light, food, water)

def manualGrow(field):
    #Get the light, water and food values from the user

    #Getting the light value
    valid = False

    while not valid:
        
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Value entered is not valid - Please enter a value between 1 and 10")
                
        except ValueError:
            print("Value entered is not valid - Please enter a value between 1 and 10")

    #Getting the water value
    valid = False

    while not valid:
        
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered is not valid - Please enter a value between 1 and 10")
                
        except ValueError:
            print("Value entered is not valid - Please enter a value between 1 and 10")

    #Getting the food value
    valid = False

    while not valid:
        try:
            food = int(input("Please enter a food value (1-100): "))
            if 1 <= food <= 100:
                valid = True
            else:
                print("Value entered not valid - Please enter a value between 1 and 100")
        except ValueError:
            print("Value entered not valid - Please enter a value between 1 and 100")

    #Grow the field
    field.grow(light, food, water)
                

def displayCrops(cropList):
    print()
    print("The following crops are in this field:")

    pos = 1

    for crop in cropList:
        print("{0:>2}. {1}".format(pos,crop.report()))
        pos += 1

def displayAnimals(animalList):
    print()
    print("The following animals are in this field:")

    pos = 1

    for animal in animalList:
        print("{0:>2}. {1}".format(pos,animal.report()))
        pos += 1

def selectCrop(lengthList):
    valid = False

    while not valid:
        while not valid:
            selected = int(input("Please select a crop: "))
            if selected in range(1,lengthList+1):
                valid = True
            else:
                print("Please select a valid option")

        return selected -1

def selectAnimal(lengthList):
    valid = False
    
    while not valid:
        selected = int(input("Please select an animal: "))
        if selected in range(1,lengthList+1):
            valid = True
        else:
            print("Please select a valid option")
            
    return selected -1

def harvestCropFromField(field):
    displayCrops(field._crops)
    selectedCrop = selectCrop(len(field._crops))

    return field.harvestCrop(selectedCrop)

def removeAnimalFromField(field):
    displayAnimals(field._animals)
    selectedAnimal = selectAnimal(len(field._animals))

    return field.removeAnimal(selectedAnimal)

def displayCropMenu():
    print()
    print("Which crop type would you like to add?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("0. I don't want to add a crop - return me to the main menu")
    print()
    print("Please select an option from the above menu")

def displayAnimalMenu():
    print()
    print("Which animal type would you like to add?")
    print()
    print("1. Cow")
    print("2. Sheep")
    print()
    print("0. I don't want to add an animal - return me to the main menu")
    print()
    print("Please select an option from the above menu")

def displayMainMenu():
    print()
    print("1. Plant a new crop")
    print("2. Harvest a crop")
    print()
    print("3. Add an animal")
    print("4. Remove an animal")
    print()
    print("5. Grow field manually over 1 day")
    print("6. Grow field automatically over 30 days")
    print()
    print("7. Report field status")
    print()
    print("8. Exit test program")
    print()
    print("Please selet an option from the above menu")

def getMenuChoice(lower, upper):
    valid = False

    while not valid:
        try:
            choice = int(input("Option selected: "))
            if lower <= choice <= upper:
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
            
    return choice

def plantCropInField(field):
    displayCropMenu()
    choice = getMenuChoice(0,2)
    
    if choice == 1:
        if field.plantCrop(Potato()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Field is full - potato not planted")
            print()
            
    elif choice == 2:
        if field.plantCrop(Wheat()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Field is full - wheat not planted")

def addAnimalToField(field):
    displayAnimalMenu()
    choice = getMenuChoice(1,2)

    if choice == 1:
        if field.addAnimal(Cow()):
            print()
            print("Cow added")
            print()
        else:
            print()
            print("Field is full - cow not planted")
            print()
            
    elif choice == 2:
        if field.addAnimal(Sheep()):
            print()
            print("Sheep added")
            print()
        else:
            print()
            print("Field is full - sheep not added")

def manageField(field):
    print("This is the field management program")
    print()

    exit = False

    while not exit:
        displayMainMenu()
        option = getMenuChoice(0,7)
        print()

        if option == 1:
            plantCropInField(field)
        elif option == 2:
            removedCrop = harvestCropFromField(field)
            print("You removed the crop: {0}".format(removedCrop))
        elif option == 3:
            addAnimalToField(field)
        elif option == 4:
            removedAnimal = removeAnimalFromField(field)
            print("You removed the animal: {0}".format(removedAnimal))
        elif option == 5:
            manualGrow(field)
        elif option == 6:
            autoGrow(field,30)
        elif option == 7:
            print(field.reportContents())
            print()
        elif option == 0:
            exit = True
            print()
            
    print("Thank you for using the field management program")

def main():
    newField = Field(5,2)

    #Task 9
    #print(newField._crops)
    #print(newField._animals)
    #print(newField._maxAnimals)
    #print(newField._maxCrops)

    #Task 10
    #newField.plantCrop(Wheat())
    #newField.addAnimal(Sheep())
    #print(newField._crops)
    #print(newField._animals)

    #newField.harvestCrop(0)
    #newField.removeAnimal(0)
    #print(newField._crops)
    #print(newField._animals)

    #newField.plantCrop(Wheat())
    #newField.plantCrop(Potato())
    #newField.addAnimal(Sheep())
    #newField.addAnimal(Cow())

    #Task 10
    #displayCrops(newField._crops)
    #displayAnimals(newField._animals)

    #Task 11
    #harvestCropFromField(newField)
    #print(newField._crops)
    #removeAnimalFromField(newField)
    #print(newField._animals)

    #Task 12
    #report = newField.reportContents()
    #print(report)
    #report = newField.reportNeeds()
    #print(report)

    #Task 13
    #newField.grow(100,10,10)

    #Task 14
    #manualGrow(newField)
    #print(newField.reportContents())

    #autoGrow(newField,30)
    #print(newField.reportContents())

    manageField(newField)

if __name__ == "__main__":
    main()
