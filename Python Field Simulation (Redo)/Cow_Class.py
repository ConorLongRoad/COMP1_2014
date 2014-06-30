from Animal_Class import *

class Cow(Animal):
    """A cow animal"""

    def __init__(self):
        #Call the parent class constructor with default values for a cow

        #Cow attributes:
        #Growth rate = 1
        #Food need = 50
        #Water need = 6

        super().__init__(1,50,6)
        self._type = "Cow"

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

    cowAnimal = Cow()

    print(cowAnimal.report())

    manualGrow(cowAnimal)
    print(cowAnimal.report())

if __name__ == "__main__":
    main()
