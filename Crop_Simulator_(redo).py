import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class crop_window(QMainWindow):
    """This class creates a main window to observe the growth of a simulated crop"""

    #Constructor
    def __init__(self):
        super().__init__() #Call super class constructor
        self.setWindowTitle("Crop Simulator") #Set window title

def main():
    cropSimulation = QApplication(sys.argv) #Creatre new application
    cropWindow = crop_window() #Create new instance of main window
    cropWindow.show() #Make instance visible
    cropWindow.raise_() #Raise instanc to top of window stack
    cropSimulation.exec_() #Monitor application for events

if __name__ == "__main__":
    main()
