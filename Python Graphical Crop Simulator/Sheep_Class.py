from Animal_Class import *

class Sheep(Animal):
    """A Sheep animal"""

    def __init__(self):
        #Call the parent class constructor with default values for a Sheep

        #Sheep attributes:
        #Growth rate = 1
        #Food need = 30
        #Water need = 5

        super().__init__(1,50,6)
        self._type = "Sheep"

    def grow(self, food, water):

        if food >= self._foodNeed and water >= self._waterNeed:
            if self._status == "Toddler" and water > self._waterNeed:
                self._weight += self._growthRate * 1.5
            elif self._status == "Young" and water > self._waterNeed:
                self._weight += self._growthRate * 1.25
            else:
                self._weight += self._growthRate

        #Add 1 day
        self._daysGrowing += 1

        #Update the status
        self.updateStatus()

def main():

    SheepAnimal = Sheep()

    print(SheepAnimal.report())

    manualGrow(SheepAnimal)
    print(SheepAnimal.report())

if __name__ == "__main__":
    main()
