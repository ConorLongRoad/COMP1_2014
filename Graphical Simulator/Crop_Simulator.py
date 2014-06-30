import sys
import random

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

        self.stackedLayout = QStackedLayout() #This holds the various layout that this layout needs
        self.stackedLayout.addWidget(self.selectCropWidget)

        #Set the central widget to display the layout
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.centralWidget)

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

    def createViewCropLayout(self, cropType):
        #This is the second layout of the window - view the crop growth
        self.growthLabel = QLabel("Growth")
        self.daysLabel = QLabel("Days Growing")
        self.statusLabel = QLabel("Status")

        self.growthLineEdit = QLineEdit()
        self.daysLineEdit = QLineEdit()
        self.statusLineEdit = QLineEdit()

        self.manualGrowButton = QPushButton("Manually Grow")
        self.automaticGrowButton = QPushButton("Automatically Grow")

        self.growGrid = QGridLayout()
        self.statusGrid = QGridLayout()

        #Add label widgets to the status layout
        self.statusGrid.addWidget(self.growthLabel, 0, 0)
        self.statusGrid.addWidget(self.daysLabel, 1, 0)
        self.statusGrid.addWidget(self.statusLabel, 2, 0)

        #Add line edit widgets to the status layout
        self.statusGrid.addWidget(self.growthLineEdit, 0, 1)
        self.statusGrid.addWidget(self.daysLineEdit, 1, 1)
        self.statusGrid.addWidget(self.statusLineEdit, 2, 1)

        #Add widgets/layouts to the grow layout
        self.growGrid.addLayout(self.statusGrid, 0, 1)
        self.growGrid.addWidget(self.manualGrowButton, 1, 0)
        self.growGrid.addWidget(self.automaticGrowButton, 1, 1)

        #Create a widget to display the grow layout
        self.viewCropWidget = QWidget()
        self.viewCropWidget.setLayout(self.growGrid)

        #Connections
        self.automaticGrowButton.clicked.connect(self.automaticallyGrowCrop)

    def instantiateCrop(self):
        cropType = self.cropRadioButtons.selectedButton() #Get the radio that was clicked

        if cropType == 1:
            self.simulatedCrop = Wheat()
        elif cropType == 2:
            self.simulatedCrop = Potato()

        self.createViewCropLayout(cropType) #Create the view crop growth layout
        self.stackedLayout.addWidget(self.viewCropWidget) #Add this to the stack
        self.stackedLayout.setCurrentIndex(1) #Change the visible layout in the stack
        
    def automaticallyGrowCrop(self):
        for days in range(30):
            light = random.randint(1,10)
            water = random.randint(1,10)
            self.simulatedCropGrow(light, water)
        
def main():
    cropSimulation = QApplication(sys.argv) #Creatre new application
    cropWindow = crop_window() #Create new instance of main window
    cropWindow.show() #Make instance visible
    cropWindow.raise_() #Raise instanc to top of window stack
    cropSimulation.exec_() #Monitor application for events

if __name__ == "__main__":
    main()
