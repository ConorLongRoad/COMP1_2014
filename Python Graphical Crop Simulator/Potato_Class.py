from Crop_Class import *

class Potato(Crop): #We do Potato(Crop), because Potato is a subclass of the Crop class
    """A potato crop"""

    def __init__(self):
        #Call the parent class constructor with default values for potato

        #Potato attributes:
        #Growth rate = 1
        #Light need = 3
        #Water need = 6

        super().__init__(1,3,6)
        self._type = "Potato"

    #Override grow method for subclass.
    #This method will take priority over the method in the Crop_Class
    def grow(self,light,water):
        
        if light >= self._lightNeed and water >= self._waterNeed:
            if self._status == "Seedling" and water > self._waterNeed:
                self._growth += self._growthRate * 1.5
            elif self._status == "Young" and water > self._waterNeed:
                self._growth += self._growthRate * 1.25
            else:
                self._growth += self._growthRate

        #Add 1 day
        self._daysGrowing += 1

        #Update the status
        self.updateStatus()
        
def main():
    #Create a new potato crop

    #Task 7
    potatoCrop = Potato()
    print(potatoCrop.report())

    #Manually grow the crop

    manualGrow(potatoCrop)
    print(potatoCrop.report())

    manualGrow(potatoCrop)
    print(potatoCrop.report())

if __name__ == "__main__":
    main()
