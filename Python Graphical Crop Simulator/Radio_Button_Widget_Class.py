from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """This class create a group of raido buttons from a given list of labels"""

    #Constructor
    def __init__(self, label, instruction, buttonList):
        #Super class constructor
        super().__init__()

        #Create widgets
        self.titleLabel = QLabel(label)
        self.radioGroupBox = QGroupBox(instruction)
        self.raidoButtonGroup = QButtonGroup()

        #Create the radio buttons
        self.radioButtonList = []
        for each in buttonList:
            #Adds a radio button for each type in the list
            #E.g. if the list contained: Wheat, Potato, Cow
            #the buttons would list as Wheat, Potato and Cow
            self.radioButtonList.append(QRadioButton(each))

        #Set teh default checked item
        self.radioButtonList[0].setChecked(True)

        #Create layout for radio buttons and add them
        self.radioButtonLayout = QVBoxLayout()

        #Add buttons to the layout and button group
        counter = 1
        for each in self.radioButtonList.addWidget(each):
            self.radioButtonLayout.addWidget(each)
            self.radioButtonGroup.addButton(each)
            self.radioButtonGroup.setId(each, counter)
            counter += 1

        #Add radio buttons to the group box
        self.radioGroupBox.setLayout(self.radioButtonLayout)

        #Create a layout for whole widget
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.titleLabel)
        self.mainLayout.addWidget(self.radioGroupBox)

        #Set the layout for this widget
        self.setLayout(self.mainLayout)

    #Method to find out the selected button
    def selectedButton(self):
        return self.radioButtonGroup.checkedId()
