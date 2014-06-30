import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Radio_Button_Widget_Class import * #Provides the radio button widget
from Wheat_Class import *
from Potato_Class import *

class crop_window(QMainWindow):
    """This class creates a main window to observe the growth of a simulated crop"""

    #Constructor
    def __init__(self):
        super().__init__() #Call super class constructor
        self.setWindowTitle("Crop Simulator") #Set window title
        self.createSelectCropLayout()

    def createSelectCropLayout(self):
        #This is the initial layout of the window - to select the crop type

        self.cropRadioButtons = RadioButtonWidget("Crop Simulation", "Please select a crop", ("Wheat","Potato"))
        self.instantiateButton = QPushButton("Create Crop")

        #Create layout to hold the widget
        self.initialLayout = QVBoxLayout()
        self.initialLayout.addWidget(self.cropRadioButtons)
        self.initialLayout.addWidget(self.instantiateButton)

        self.selectCropWidget = QWidget()
        self.selectCropWidget.setLayout(self.initialLayout)

        self.setCentralWidget(self.selectCropWidget)

        #Connections
        self.instantiateButton.clicked.connect(self.instantiateCrop)

    def instantiateCrop(self):
        cropType = self.cropRadioButtons.selectedButton() #Get the radio that was clicked

        if cropType == 1:
            self.simulatedCrop = Wheat()
        elif cropType == 2:
            self.simulatedCrop = Potato()
        print(self.simulatedCrop)
        
def main():
    cropSimulation = QApplication(sys.argv) #Creatre new application
    cropWindow = crop_window() #Create new instance of main window
    cropWindow.show() #Make instance visible
    cropWindow.raise_() #Raise instanc to top of window stack
    cropSimulation.exec_() #Monitor application for events

if __name__ == "__main__":
    main()
