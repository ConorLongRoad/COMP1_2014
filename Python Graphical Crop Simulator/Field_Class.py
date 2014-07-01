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

    newField.plantCrop(Wheat())
    newField.plantCrop(Potato())
    newField.addAnimal(Sheep())
    newField.addAnimal(Cow())

    #Task 10
    #displayCrops(newField._crops)
    #displayAnimals(newField._animals)

    harvestCropFromField(newField)
    print(newField._crops)

    removeAnimalFromField(newField)
    print(newField._animals)

if __name__ == "__main__":
    main()
