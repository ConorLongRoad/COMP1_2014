from Crop_Class import *

class Wheat(Crop): #We do Wheat(Crop), because Wheat is a subclass of the Crop class
    """A wheat crop"""

    def __init__(self):
        #Call the parent class constructor with default values for wheat

        #Wheat attributes:
        #Growth rate = 1
        #Light need = 2
        #Water need = 4

        super().__init__(1,2,4)
        self._type = "Wheat"

    #Override grow method for subclass.
    #This method will take priority over the method in the Crop_Class
    def grow(self,light,water):
        
        if light >= self._lightNeed and water >= self._waterNeed:
            if self._status == "Seedling" and water > self._waterNeed:
                self._growth += self._growthRate *1.5
            elif self._status == "Young" and water > self._waterNeed:
                self._growth += self._growthRate * 1.25
            else:
                self._growth += self._growthRate

        #Add 1 day
        self._daysGrowing += 1

        #Update the status
        self.updateStatus()
def main():
    #Create a new wheat crop

    #Task 7
    wheatCrop = Wheat()
    print(wheatCrop.report())

    #Manually grow the crop

    manualGrow(wheatCrop)
    print(wheatCrop.report())

    manualGrow(wheatCrop)
    print(wheatCrop.report())

if __name__ == "__main__":
    main()
